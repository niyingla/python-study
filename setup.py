from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but if you know they are missing, you can add them here
build_exe_options = {"packages": [],"excludes": ["certifi"],"include_files": []}

setup(
    name="获取区县人口",
    version="0.1",
    description="Your application description",
    options={"build_exe": build_exe_options},
    executables=[Executable("huohuo1.py")]
)