# 一、创建 conda 虚拟环境
``` bash
    # 创建
    conda create -n py310_keras python=3.10

    # 激活
    conda activate py310_keras 

    # 安装包
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple keras tensorflow numpy pandas matplotlib jupyterlab scikit-learn
```

# 二、在 Jupyter 中使用虚拟环境
``` bash
    # 把 py310_keras conda 环境注册成 Jupyter 的 kernel
    conda install ipykernel
    python -m ipykernel install --user --name py310_keras --display-name "Python (py310_keras)"

    # 启动 jupyter
    jupyter lab

    # 选择之前注册的 Python (py310_keras) 内核就行
 ```
