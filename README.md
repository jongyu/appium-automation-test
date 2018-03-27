# Appium自动化测试

## 工具安装

- Appium

```commandline
npm config set registry https://registry.npm.taobao.org
npm i -g appium
npm i -g wd
```

- Python

```commandline
pip install pipenv
```

- 依赖

```commandline
pipenv --python 2.7
pipenv install --dev
pipenv install Appium-Python-Client
pipenv install ConfigParser
pipenv install PyYAML
```

- 查看环境

```commandline
pipenv --py
```

- [HTMLTestRunner](http://tungwaiyip.info/software/HTMLTestRunner.html)
> 将`HTMLTestRunner.py`下载并拷贝到`Python/Lib/site-packages/`目录下<br>
> 将`test_HTMLTestRunner.py`下载并拷贝到`Python/Lib/site-packages/`目录下<br>