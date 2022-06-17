import pickle
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

def save_list(save_list, filename):
    with open(filename, 'wb') as f:
    pickle.dump(save_list, f)

def load_list(filename):
    with open(filename, 'rb') as f:
    train_data = pickle.load(f)

def show_tsne():
    tsne = TSNE(n_components=2)
    X = tsne.fit_transform(X_show)
    
    df = pd.DataFrame(X, index=word_show, columns=['x', 'y'])
    fig = plt.figure()
    fig.set_size_inches(30, 20)
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(df['x'], df['y'])
    
    for word, pos in df.iterrows():
        ax.annotate(word, pos, fontsize=10)
    
    plt.xlabel("t-SNE 특성0")
    plt.ylabel("t-SNE 특성1")
    plt.show()
