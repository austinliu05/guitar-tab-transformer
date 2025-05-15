import json

with open("/home/claudehu/Desktop/repo/guitar-tab-transformer/backend/tab-processing/misc/_DadaGP_song_tokens_frequency.json", "r") as f:
    token_stats = json.load(f)

bfx_stats = {token: count for token, count in token_stats.items() if "bfx" in token}
nfx_stats = {token: count for token, count in token_stats.items() if "nfx" in token}
param_stats = {token: count for token, count in token_stats.items() if "param" in token}