# A small game called `'Aliens invasion'` written in Python
This project is just a replica.  


[![language](https://img.shields.io/badge/Language-Python%203.11.3-yellow?style=plastic&logo=appveyor)](https://docs.python.org/3/)
[![]()]()
[![pygame](https://img.shields.io/badge/Powered%20%20by-Pygame%202.1.3-brightgreen?style=plastic&logo=appveyor)](https://www.pygame.org/docs/)
[![](https://img.shields.io/badge/OS-Arch%20linux-informational?style=plastic&logo=appveyor)](https://archlinux.org/)
## Environment
### Arch linux
```shell
# sudo pacman -Sy python
sudo pacman -Sy python-pygame
```
### Windows
Via `pip`(a package manager for python library)(Official Recommanded)
```Power shell
python3 -m pip install -U pygame --user
```
### To see if it works
Run:
```shell
python3 -m pygame.examples.aliens
```
## Image

| **\\**          | **image**                                |
|:---------------:|:----------------------------------------:|
|   Ships         | <img src="images/ships.png" alt="ships"> |
|   Aliens        | <img src="images/alien.png" alt="alien"> |
|   Other style   | <img src="images/jinx.png" alt="jinx">   |

## Files
| **File**                             | **Function**                         |
|:------------------------------------:|:------------------------------------:|
| alien_invasion.py                    | main function                        |
| game_function.py                     | the most functions for running game  |
| game_stats.py                        | class for recording game information |
| settings.py                          | the property of game                 |
| scoreboard.py                        | show the score                       |
| alien.py bullet.py ship.py button.py | class alien, bullet, ship, button    |