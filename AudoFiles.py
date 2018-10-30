import pygame
import random

'''
-------------------------------------------------------------------------------
Audio file dictionary
-------------------------------------------------------------------------------
'''

AudioDict = {}

AudioDict['open_menu_sound'] = pygame.mixer.Sound(
    'Resources/Audio/Sounds/open_menu.wav')

AudioDict['close_menu_sound'] = pygame.mixer.Sound(
    'Resources/Audio/Sounds/close_menu.wav')

AudioDict['press_button_sound'] = pygame.mixer.Sound(
    'Resources/Audio/Sounds/press_button.wav')

AudioDict['switch_lanes_sound'] = pygame.mixer.Sound(
    'rgegeg.wav')

AudioDict['sword_swing_sound'] = pygame.mixer.Sound(
    'Resources/Audio/Sounds/sword_swing.wav')

AudioDict['damaging_enemy_sounds'] = \
    [pygame.mixer.Sound('Resources/Audio/Sounds/damage_enemy_1.wav'),
     pygame.mixer.Sound('Resources/Audio/Sounds/damage_enemy_2.wav'),
     pygame.mixer.Sound('Resources/Audio/Sounds/damage_enemy_3.wav'),
     pygame.mixer.Sound('Resources/Audio/Sounds/damage_enemy_4.wav'),
     pygame.mixer.Sound('Resources/Audio/Sounds/damage_enemy_5.wav')
     ]

AudioDict['killing_enemy_sounds'] = \
    [pygame.mixer.Sound('dsfgsd.mp4'),
     pygame.mixer.Sound('dsfgdssd.mp4')
     ]

AudioDict['enemy_idle_sound'] = \
    [pygame.mixer.Sound('dsfgsd.mp4'),
     pygame.mixer.Sound('dsfgdssd.mp4')
     ]