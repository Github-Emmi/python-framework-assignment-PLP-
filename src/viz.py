import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import pandas as pd

# Set professional style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

def plot_publications_by_year(df, year_range=(2019, 2022)):
    """Plot publications by year with annotations"""
    df_filtered = df[(df['publish_year'] >= year_range[0]) & (df['publish_year'] <= year_range[1])]
    yearly_counts = df_filtered['publish_year'].value_counts().sort_index()
    
    fig, ax = plt.subplots()
    bars = ax.bar(yearly_counts.index.astype(str), yearly_counts.values, 
                  color=sns.color_palette("viridis", len(yearly_counts)))
    
    # Add value annotations on bars (Standout Tip)
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:,}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontweight='bold')
    
    plt.title('Publications by Year', fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Number of Publications')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def plot_top_journals(df, top_n=10):
    """Plot top journals by publication count"""
    top_journals = df['journal'].value_counts().head(top_n)
    
    fig, ax = plt.subplots()
    sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax, palette="rocket_r")
    ax.set_xlabel('Number of Publications')
    ax.set_ylabel('')
    ax.set_title(f'Top {top_n} Journals by Publication Count', fontweight='bold')
    
    # Add value labels
    for i, v in enumerate(top_journals.values):
        ax.text(v + 10, i, f' {v:,}', va='center', fontweight='bold')
    plt.tight_layout()
    return fig

def plot_title_wordcloud(df):
    """Generate a word cloud from paper titles"""
    # Combine all titles
    all_titles = ' '.join(df['title_clean'].dropna().astype(str))
    
    # Remove common stopwords
    stopwords = set(['the', 'and', 'of', 'in', 'a', 'to', 'for', 'with', 'on', 'by', 'an'])
    wordcloud = WordCloud(stopwords=stopwords, width=800, height=400, 
                          background_color='white').generate(all_titles)
    
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('Most Frequent Words in Titles', fontweight='bold')
    plt.tight_layout()
    return fig

def plot_top_authors(df, top_n=15):
    """Plot top authors by publication count (Advanced Viz - Standout Tip)"""
    # Extract first author from author lists
    df_first_author = df.dropna(subset=['authors']).copy()
    df_first_author['first_author'] = df_first_author['authors'].apply(
        lambda x: x.split(';')[0].strip() if ';' in str(x) else str(x)
    )
    
    top_authors = df_first_author['first_author'].value_counts().head(top_n)
    
    fig, ax = plt.subplots()
    sns.barplot(x=top_authors.values, y=top_authors.index, ax=ax, palette="mako_r")
    ax.set_xlabel('Number of Publications')
    ax.set_ylabel('')
    ax.set_title(f'Top {top_n} Authors by Publication Count', fontweight='bold')
    
    # Add value labels
    for i, v in enumerate(top_authors.values):
        ax.text(v + 10, i, f' {v:,}', va='center', fontweight='bold')
    plt.tight_layout()
    return fig