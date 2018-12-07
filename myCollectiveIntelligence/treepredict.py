from PIL import Image,ImageDraw
#预测网站的用户行为及购买决策
my_data=[['slashdot','USA','yes',18,'None'],
         ['google','France','yes',23,'Premium'],
         ['digg','USA','yes',24,'Basic'],
         ['kiwitobes','France','yes',23,'Basic'],
         ['google','UK','no',21,'Premium'],
         ['(direct)','New Zealand','no',12,'None'],
         ['(direct)','UK','no',21,'Basic'],
         ['google','USA','no',24,'Premium'],
         ['slashdot','France','yes',19,'None'],
         ['digg','USA','no',18,'None'],
         ['google','UK','no',18,'None'],
         ['kiwitobes','UK','no',19,'None'],
         ['digg','New Zealand','yes',12,'Basic'],
         ['google','UK','yes',18,'Basic'],
         ['kiwitobes','France','yes',19,'Basic']]

#构造决策树的表达形式
class decisionnode:
    def __init__(self,col=-1,value=None,results=None,tb=None,fb=None):
        self.col=col #待检验的判断条件所对应的列索引值，对哪一列进行判断
        self.value=value #为使结果为true，当前列对应的值
        self.results=results #保存分支的结果，除叶节点外，在其他节点上，该值为None
        self.tb=tb  #判断条件为true时，当前节点的子节点
        self.fb=fb  #判断条件为false时，当前节点的子节点

#基于某一特征对数据集拆分，能够处理数值型或名词性数据
#rows表示样本集，column匹配的属性列索引，value指定列上的数据值
def divideset(rows,column,value):
    #定义一函数，数据行属于第一组还是第二组，返回分别为true和false
    split_function=None
    if isinstance(value,int) or isinstance(value,float):
        #数值型按大于，小于来区分，字符串为等于，不等于区分
        split_function=lambda row:row[column]>=value #lambda函数也叫匿名函数，即，函数没有具体的名称,而用def创建的方法是有名称的。
#lambda允许用户快速定义单行函数，当然用户也可以按照典型的函数定义完成函数。lambda的目的就是简化用户定义使用函数的过程。
    else:
        split_function=lambda row:row[column]==value

    #将数据集拆分成两个集合，并返回
    set1=[row for row in rows if split_function(row)]
    set2=[row for row in rows if not split_function(row)]
    return (set1,set2)
#对各种可能的结果进行计数（在每行的最后一列放置）
def uniquecounts(rows):
    results={ }
    for row in rows:
        #计数结果放置在最后一列
        r=row[len(row)-1]
        if r not in results: results[r]=0
        results[r]+=1
    return results

#基尼不纯度
def giniimpurity(rows):
    total=len(rows)
    counts=uniquecounts(rows)
    imp=0
    for k1 in counts:
        p1=float(counts[k1])/total #取值为k1的概率
        for k2 in counts:
            if k1==k2: continue
            p2=float(counts[k2])/total #取值为k2的概率
            imp+=p1*p2
        return imp

#熵
def entropy(rows):
    from math import log
    log2=lambda x:log(x)/log(2)#以2为底的对数
    results=uniquecounts(rows)
    #计算熵的值
    ent=0.0
    for r in results.keys():
        p=float(results[r])/len(rows) #概率
        ent=ent-p*log2(p)#公式
    return ent

#信息增益，选择合适的特征来拆分
def buildtree(rows,scoref=entropy):
    if len(rows)==0: return decisionnode()
    current_score=scoref(rows)

    #记录最佳拆分条件，信息增益最大
    best_gain=0.0
    best_criteria=None
    best_sets=None

    column_count=len(rows[0])-1 #列数
    for col in range(0,column_count):#遍历每一列
        #每列的可能取不同值构成的序列
        column_values={ }
        for row in rows:
            column_values[row[col]]=1
        #根据列中的每个值，对数据集进行拆分
        for value in column_values.keys():
            (set1,set2)=divideset(rows,col,value)
            #信息增益
            p=float(len(set1))/len(rows)
            gain=current_score-p*scoref(set1)-(1-p)*scoref(set2)
            if gain>best_gain and len(set1)>0 and len(set2)>0:
                best_gain=gain
                best_criteria=(col,value)
                best_sets=(set1,set2)
        #创建子分支
    if best_gain>0:
        trueBranch=buildtree(best_sets[0]) #创建左分支
        falseBranch=buildtree(best_sets[1]) #创建右分支
        return decisionnode(col=best_criteria[0],value=best_criteria[1],tb=trueBranch,fb=falseBranch)
    else:
        return decisionnode(results=uniquecounts(rows))

    #决策树的显示
def printtree(tree,indent=''):
    if tree.results!=None: #叶节点非空
        print(str(tree.results))
    else:
        #打印判断条件
        print(str(tree.col)+':'+str(tree.value)+'?')
        #打印分支
        print(indent+'T->',printtree(tree.tb,indent+' '))
        print(indent+'F->',printtree(tree.fb,indent+' '))

#树的宽度
def getwidth(tree):
    if tree.tb==None and tree.fb==None:return 1
    return getwidth(tree.tb)+getwidth(tree.fb)
#树的深度
def getdepth(tree):
    if tree.tb==None and tree.fb==None:return 0
    return max(getdepth(tree.tb),getdepth(tree.fb))+1
#为待绘制的树确定一个合理的尺寸，设置好画布
def drawtree(tree,jpeg='tree.jpg'):
    w=getwidth(tree)*100
    h=getdepth(tree)*100+120

    img=Image.new('RGB',(w,h),(255,255,255))
    draw=ImageDraw.Draw(img)

    drawnode(draw,tree,w/2,20) #根节点坐标
    img.save(jpeg,'JPEG')
#递归的方式绘制决策树的节点
def drawnode(draw,tree,x,y):
    if tree.results==None:
        #得到每个分支的宽度
        w1=getwidth(tree.fb)*100
        w2=getwidth(tree.tb)*100

        #确定此节点所要占据的总空间
        left=x-(w1+w2)/2
        right=x+(w1+w2)/2
        #绘制判断条件字符串
        draw.text((x-20,y-10),str(tree.col)+':'+str(tree.value),(0,0,0))
        #绘制到分支的连线
        draw.line((x,y,left+w1/2,y+100),fill=(255,0,0))
        draw.line((x,y,right-w2/2,y+100),fill=(255,0,0))
        #绘制分支的节点
        drawnode(draw,tree.fb,left+w1/2,y+100)
        drawnode(draw,tree.tb,right-w2/2,y+100)
    else:
        txt='\n'.join(['%s:%d'%v for v in tree.results.items()])
        draw.text((x-20,y),txt,(0,0,0))

#对新的观测数据进行分类
def classify(observation,tree):
    if tree.results!=None:
        return tree.results
    else:
        v=observation[tree.col]
        branch=None
        if isinstance(v,int) or isinstance(v,float):
            if v>=tree.value:branch=tree.tb
            else:branch=tree.fb
        else:
            if v==tree.value:branch=tree.tb
            else:branch=tree.fb
        return classify(observation,branch)

#剪枝，margain
def prune(tree,mingain):
    #如果分支不是叶结点，则对其进行剪枝操作
    if tree.tb.results==None: #none就表示不是叶节点
        prune(tree.tb,mingain)
    if tree.fb.results==None:
        prune(tree.fb,mingain)

    #如果两个子支都是叶节点，则判断他们是否需要合并
    if tree.tb.results!=None and tree.fb.results!=None: #就是叶节点
        #构造合并后的数据集
        tb,fb=[],[]
        for v,c in tree.tb.results.items():
            tb+=[[v]]*c #
        for v,c in tree.fb.results.items():
            fb+=[[v]]*c #
        #检查熵的减少情况
        delta=entropy(tb+fb)-(entropy(tb)+entropy(fb)/2)

        if delta<mingain:
            #合并分支
            tree.tb,tree.fb=None,None
            tree.results=uniquecounts(tb+fb)

#处理缺失数据,observation信息缺失的数据项
def mdclassify(observation,tree):
    if tree.results!=None: #叶节点
        return tree.results
    else:
        v=observation[tree.col] #获取数据的列
        if v==None: #若列数据缺失，对左右子树分别分类
            tr,fr=mdclassify(observation,tree.tb),mdclassify(observation,tree.fb)
            #在某属性上没有缺失值的总样本数
            tcount=sum(tr.values())
            fcount=sum(fr.values())
            #占总样本的比例，得到左右子树的权重
            tw=float(tcount)/(tcount+fcount)
            fw=float(fcount)/(tcount+fcount)
            result={}
            #左右子树的加权
            for k,v in tr.items():result[k]=v*tw
            for k,v in fr.items():
                if k not in result:result[k]=0
                result[k]+=v*fw
            return result
        #没有缺失值，继续分类
        else:
            if isinstance(v,int) or isinstance(v,float):
                if v>=tree.value:branch=tree.tb
                else:branch=tree.fb
            else:
                if v==tree.value:branch=tree.tb
                else:branch=tree.fb
            return mdclassify(observation,branch)

#处理数值型结果
#使用方差作为评价函数来取代熵或基尼不纯度
def variance(rows):
    if len(rows)==0:return 0
    data=[float(row[len(row)-1]) for row in rows]
    mean=sum(data)/len(data)
    variance=sum([(d-mean)**2 for d in data])/len(data)
    return variance


#tree=treepredict.buildtree(treepredict.my_data)
