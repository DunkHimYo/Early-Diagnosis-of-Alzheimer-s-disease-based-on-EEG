from sklearn.decomposition import NMF
import seaborn as sns

nmf=NMF(n_components=1, random_state=0)
data['nmf']=nmf.fit_transform(X=data[roi])

g=sns.boxplot(data=data, hue='Group0',x='PS',y='nmf',showfliers=False)
g.set_title('ROI Reduction Using NMF')
g.set_ylabel("Sample Entropy")
handles,labels=g.get_legend_handles_labels()
g.legend(handles,['HC','MCI','AD'])
