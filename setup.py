import setuptools

setuptools.setup(
    name="pystocktwits_data_utils",
    version="0.0.3",
    author="Kalani Murakami",
    author_email="kalanimurakami1218@gmail.com",
    description="Data Utils for Unofficial Python Wrapper StockTwits API",
    packages=['pystocktwits', 'pystocktwits_data_utils'],
    install_requires=["requests"],
    license="MIT",
    url="https://github.com/khmurakami/pystocktwits_data_utils"
)
