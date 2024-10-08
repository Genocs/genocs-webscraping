<!-- PROJECT SHIELDS -->
[![License][license-shield]][license-url]
[![Build][build-shield]][build-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Discord][discord-shield]][discord-url]
[![Gitter][gitter-shield]][gitter-url]
[![Twitter][twitter-shield]][twitter-url]
[![Twitterx][twitterx-shield]][twitterx-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[license-shield]: https://img.shields.io/github/license/Genocs/genocs-webscraping?color=2da44e&style=flat-square
[license-url]: https://github.com/Genocs/genocs-webscraping/blob/main/LICENSE
[build-shield]: https://github.com/Genocs/genocs-webscraping/actions/workflows/build_and_test.yml/badge.svg?branch=main
[build-url]: https://github.com/Genocs/genocs-webscraping/actions/workflows/build_and_test.yml
[contributors-shield]: https://img.shields.io/github/contributors/Genocs/genocs-webscraping.svg?style=flat-square
[contributors-url]: https://github.com/Genocs/genocs-webscraping/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Genocs/genocs-webscraping?style=flat-square
[forks-url]: https://github.com/Genocs/genocs-webscraping/network/members
[stars-shield]: https://img.shields.io/github/stars/Genocs/genocs-webscraping.svg?style=flat-square
[stars-url]: https://img.shields.io/github/stars/Genocs/genocs-webscraping?style=flat-square
[issues-shield]: https://img.shields.io/github/issues/Genocs/genocs-webscraping?style=flat-square
[issues-url]: https://github.com/Genocs/genocs-webscraping/issues
[discord-shield]: https://img.shields.io/discord/1106846706512953385?color=%237289da&label=Discord&logo=discord&logoColor=%237289da&style=flat-square
[discord-url]: https://discord.com/invite/fWwArnkV
[gitter-shield]: https://img.shields.io/badge/chat-on%20gitter-blue.svg
[gitter-url]: https://gitter.im/genocs/
[twitter-shield]: https://img.shields.io/twitter/follow/genocs?color=1DA1F2&label=Twitter&logo=Twitter&style=flat-square
[twitter-url]: https://twitter.com/genocs
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/giovanni-emanuele-nocco-b31a5169/
[twitterx-shield]: https://img.shields.io/twitter/url/https/twitter.com/genocs.svg?style=social
[twitterx-url]: https://twitter.com/genocs

<p align="center">
    <img src="./assets/genocs-library-logo.png" alt="icon">
</p>

# Web Scraping Web Api 
Simple Web Scraping WebApi based on Flask.

## Goals


## Prerequisites

## Getting Started

Tested with:

> - python 3.9.13
> - pip 23.2.1

## Build and run locally
    
```bash
pip install -r requirements.txt
pip install --upgrade gevent
cd ./src
python main.py
```


# Description

This project is usign Flask along with other libraries.
- [flask-restful](https://flask-restful.readthedocs.io/)

- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [requests](https://docs.python-requests.org/en/master/)
- [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/)






## Build Docker Image

```bash
docker build -t genocs/scraping-webapi:latest -t genocs/scraping-webapi:1.0.0 .
docker run --name scraping-webapi-container -p 5400:5400 genocs/scraping-webapi:1.0.0
docker compose up
docker push genocs/scraping-webapi:1.0.0
docker push genocs/scraping-webapi:latest
```

## License

This project is licensed with the [MIT license](LICENSE).

## Changelogs

View Complete [Changelogs](https://github.com/Genocs/microservice-template/blob/main/CHANGELOGS.md).

## Community

- Discord [@genocs](https://discord.com/invite/fWwArnkV)
- Facebook Page [@genocs](https://facebook.com/Genocs)
- Youtube Channel [@genocs](https://youtube.com/c/genocs)


## Support

Has this Project helped you learn something New? or Helped you at work?
Here are a few ways by which you can support.

- ⭐ Leave a star!
- 🥇 Recommend this project to your colleagues.
- 🦸 Do consider endorsing me on LinkedIn for ASP.NET Core - [Connect via LinkedIn](https://www.linkedin.com/in/giovanni-emanuele-nocco-b31a5169/)
- ☕ If you want to support this project in the long run, [consider buying me a coffee](https://www.buymeacoffee.com/genocs)!

[![buy-me-a-coffee](https://raw.githubusercontent.com/Genocs/genocs-webscraping/main/assets/buy-me-a-coffee.png "buy-me-a-coffee")](https://www.buymeacoffee.com/genocs)

## Code Contributors

This project exists thanks to all the people who contribute. [Submit your PR and join the team!](CONTRIBUTING.md)

[![genocs contributors](https://contrib.rocks/image?repo=Genocs/genocs-webscraping "genocs contributors")](https://github.com/genocs/genocs-webscraping/graphs/contributors)

## Financial Contributors

Become a financial contributor and help me sustain the project. [Support the Project!](https://opencollective.com/genocs/contribute)

<a href="https://opencollective.com/genocs"><img src="https://opencollective.com/genocs/individuals.svg?width=890"></a>

## Acknowledgements
