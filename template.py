import os

# Cây thư mục chuẩn
structure = {
    "src": ["__init__.py", "main.py"],
    "src/api": [],
    "src/trading": [],
    "src/utils": [],
    "tests": ["test_trading.py"],
    "data": ["sample_trades.json"],
    "docs": ["architecture.md"],
}

files = [".gitignore", "requirements.txt", "README.md"]

# Tạo thư mục và file
for folder, fs in structure.items():
    os.makedirs(folder, exist_ok=True)
    for f in fs:
        open(os.path.join(folder, f), "w").close()

for f in files:
    open(f, "w").close()

print("✅ Project structure created!")