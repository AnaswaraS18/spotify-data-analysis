import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('/kaggle/input/datasets/maharshipandya/-spotify-tracks-dataset/dataset.csv')
df = df.dropna()
df = df.reset_index(drop=True)
print("✅ Data loaded! Total songs:", len(df))
df.head()

top_genres = df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('white')
ax.set_facecolor('#f8f8f8')

colors = ['#1DB954' if i > 0 else '#FF6B35' for i in range(len(top_genres))]
bars = ax.bar(top_genres.index, top_genres.values, color=colors, edgecolor='white', linewidth=1.2, zorder=3)

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f'{bar.get_height():.1f}', ha='center', va='bottom',
            fontsize=11, fontweight='bold', color='#191414')

ax.set_title('Top 10 Most Popular Genres on Spotify', fontsize=18,
             fontweight='bold', color='#191414', pad=20)
ax.set_xlabel('Genre', fontsize=12, color='#535353', labelpad=10)
ax.set_ylabel('Average Popularity Score (0-100)', fontsize=12, color='#535353', labelpad=10)
ax.tick_params(colors='#535353', labelsize=11)
ax.yaxis.grid(True, linestyle='--', alpha=0.5, color='white', zorder=0)
for spine in ax.spines.values():
    spine.set_visible(False)

plt.xticks(rotation=40, ha='right')
fig.text(0.99, 0.01, 'Source: Spotify Tracks Dataset | Kaggle',
         ha='right', fontsize=9, color='#535353')
plt.tight_layout()
plt.savefig('chart1_genres.png', dpi=200, bbox_inches='tight')
plt.show()
print("✅ Chart 1 saved!")

sample = df.sample(5000, random_state=42)

fig, ax = plt.subplots(figsize=(10, 7))
fig.patch.set_facecolor('white')
ax.set_facecolor('#f8f8f8')

scatter = ax.scatter(sample['energy'], sample['popularity'],
                     alpha=0.4, c=sample['energy'],
                     cmap='RdYlGn', edgecolors='none', s=20, zorder=3)

cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Energy Level', fontsize=11, color='#535353')

ax.set_title('Does High Energy = More Popular?', fontsize=18,
             fontweight='bold', color='#191414', pad=20)
ax.set_xlabel('Energy Level  (0 = Calm  →  1 = Intense)', fontsize=12,
              color='#535353', labelpad=10)
ax.set_ylabel('Popularity Score (0-100)', fontsize=12, color='#535353', labelpad=10)
ax.tick_params(colors='#535353', labelsize=11)
ax.yaxis.grid(True, linestyle='--', alpha=0.5, color='white', zorder=0)
ax.xaxis.grid(True, linestyle='--', alpha=0.5, color='white', zorder=0)
for spine in ax.spines.values():
    spine.set_visible(False)

fig.text(0.99, 0.01, 'Source: Spotify Tracks Dataset | Kaggle',
         ha='right', fontsize=9, color='#535353')
plt.tight_layout()
plt.savefig('chart2_energy.png', dpi=200, bbox_inches='tight')
plt.show()
print("✅ Chart 2 saved!")

top_dance = df.groupby('track_genre')['danceability'].mean().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('white')
ax.set_facecolor('#f8f8f8')

colors = ['#FF6B35' if i == len(top_dance)-1 else '#1DB954' for i in range(len(top_dance))]
bars = ax.barh(top_dance.index, top_dance.values, color=colors,
               edgecolor='white', linewidth=1.2, zorder=3)

for bar in bars:
    ax.text(bar.get_width() + 0.002, bar.get_y() + bar.get_height()/2,
            f'{bar.get_width():.3f}', va='center',
            fontsize=11, fontweight='bold', color='#191414')

ax.set_title('Top 10 Most Danceable Genres on Spotify', fontsize=18,
             fontweight='bold', color='#191414', pad=20)
ax.set_xlabel('Average Danceability Score (0-1)', fontsize=12,
              color='#535353', labelpad=10)
ax.set_ylabel('Genre', fontsize=12, color='#535353', labelpad=10)
ax.tick_params(colors='#535353', labelsize=11)
ax.xaxis.grid(True, linestyle='--', alpha=0.5, color='white', zorder=0)
for spine in ax.spines.values():
    spine.set_visible(False)

fig.text(0.99, 0.01, 'Source: Spotify Tracks Dataset | Kaggle',
         ha='right', fontsize=9, color='#535353')
plt.tight_layout()
plt.savefig('chart3_danceability.png', dpi=200, bbox_inches='tight')
plt.show()
print("✅ Chart 3 saved!")

