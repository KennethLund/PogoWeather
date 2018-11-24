#!/usr/bin/env python3

from urllib.request import urlopen
import json
import time 
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

 
client = discord.Client
bot = commands.Bot(command_prefix='+')
 
@bot.event
async def on_ready():
    print('At your service master')
 
@bot.command()
async def saymyname():
    '''test if bot is online.'''
    await bot.say('Hello, world! Oh fuck, thats not what you wanted')
 
@bot.command()
async def weather12():
    url  = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/124594?apikey=FSAQAI4wiFTwxVQjj8IEmGKFSO37gHF4&details=true&metric=true%20HTTP/1.1'

    obj  = urlopen(url)
    data = json.load(obj)
    localtime = time.asctime( time.localtime(time.time()) )
    forcast = ['The local weather for the next 12 hours will be:\n','Date: \t\t\tTime: \tWeather:']

    for times in range(12):
        item = data[times]
        datetime = item['DateTime']
        weather = item['IconPhrase']
        wind = item['Wind']['Speed']['Value']

        ingame = []

        if weather == 'Partly sunny' or weather == 'Intermittent clouds' or weather == 'Partly cloudy' or weather == 'Partly sunny w/ Showers' or weather == 'Partly Cloudy w/ Showers' or weather == 'Partly sunny w/ Flurries' or weather == 'Partly sunny w/ T-Storms' or weather == 'Partly Cloudy w/ T-Storms':
            ingame = 'Partly cloudy'
        else:
            ingame = ingame
            
        if weather == 'Mostly cloudy' or weather == 'Cloudy' or weather == 'Mostly cloudy w/ showers' or weather == 'Mostly cloudy w/ T-Storms' or weather == 'Mostly cloudy w/ Flurries' or weather == 'Hazy Sunshine' or weather == 'Hazy Moonlight':
            ingame = 'Cloudy'
        else:
            ingame = ingame

        if weather == 'Sunny' or weather == 'Clear' or weather == 'Mostly sunny' or weather == 'Mostly clear':
            ingame = 'Clear'
        else:
            ingame = ingame

        if weather == 'Fog':
            ingame = 'Fog'
        else:
            ingame = ingame

        if weather == 'Showers' or weather == 'Rain' or weather == 'T-Storms':
            ingame = 'Rainy'
        else:
            ingame = ingame

        if weather == 'Rain and Snow' or weather == 'Flurries' or weather == 'Snow':
            ingame = 'Snowy'
        else:
            ingame = ingame
            
        if wind > 14.91:
            ingame = 'Windy'
        else:
            ingame = ingame
            
        forcast.extend([datetime[:10] + '\t' + datetime[11:16] + '\t' + ingame])
    await bot.say('\n'.join(forcast))

@bot.command()
async def weatherwind():
    url  = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/124594?apikey=sD1RODtbRUAdED92mbka7PHh7YfoeJuO&details=true&metric=true%20HTTP/1.1'
    #url  = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/647339?apikey=FSAQAI4wiFTwxVQjj8IEmGKFSO37gHF4&details=true&metric=true%20HTTP/1.1'
    #await bot.say('This forecast is forecast is for Tilst')

    obj  = urlopen(url)
    data = json.load(obj)
    localtime = time.asctime( time.localtime(time.time()) )
    forcast = ['The local weather for the next 12 hours will be:\n','Date: \t\t\tTime: \tWeather: \tWind:']

    for times in range(12):
        item = data[times]
        datetime = item['DateTime']
        weather = item['IconPhrase']
        wind = item['Wind']['Speed']['Value']

        ingame = []

        if weather == 'Partly sunny' or weather == 'Intermittent clouds' or weather == 'Partly cloudy' or weather == 'Partly sunny w/ Showers' or weather == 'Partly Cloudy w/ Showers' or weather == 'Partly sunny w/ Flurries' or weather == 'Partly sunny w/ T-Storms' or weather == 'Partly Cloudy w/ T-Storms':
            ingame = 'Partly cloudy'
        else:
            ingame = ingame
            
        if weather == 'Mostly cloudy' or weather == 'Cloudy' or weather == 'Mostly cloudy w/ showers' or weather == 'Mostly cloudy w/ T-Storms' or weather == 'Mostly cloudy w/ Flurries' or weather == 'Hazy Sunshine' or weather == 'Hazy Moonlight':
            ingame = 'Cloudy'
        else:
            ingame = ingame

        if weather == 'Sunny' or weather == 'Clear' or weather == 'Mostly sunny' or weather == 'Mostly clear':
            ingame = 'Clear'
        else:
            ingame = ingame

        if weather == 'Fog':
            ingame = 'Fog'
        else:
            ingame = ingame

        if weather == 'Showers' or weather == 'Rain' or weather == 'T-Storms':
            ingame = 'Rainy'
        else:
            ingame = ingame

        if weather == 'Rain and Snow' or weather == 'Flurries' or weather == 'Snow':
            ingame = 'Snowy'
        else:
            ingame = ingame
            
        if wind > 14.91:
            ingame = 'Windy'
        else:
            ingame = ingame
            
        forcast.extend([datetime[:10] + '\t' + datetime[11:16] + '\t' + ingame + '\t' + str(wind)])
    forcast.extend(['\nWinds above 14.9 mph will result in windy weather'])
    await bot.say('\n'.join(forcast))

    
@bot.command()
async def weathertilst():
    #url  = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/124594?apikey=sD1RODtbRUAdED92mbka7PHh7YfoeJuO&details=true&metric=true%20HTTP/1.1'
    url  = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/647339?apikey=FSAQAI4wiFTwxVQjj8IEmGKFSO37gHF4&details=true&metric=true%20HTTP/1.1'
    await bot.say('This forecast is forecast is for Tilst\n')

    obj  = urlopen(url)
    data = json.load(obj)
    localtime = time.asctime( time.localtime(time.time()) )
    forcast = ['The local weather for the next 12 hours will be:\n','Date: \t\t\tTime: \tWeather: \tWind:']

    for times in range(12):
        item = data[times]
        datetime = item['DateTime']
        weather = item['IconPhrase']
        wind = item['Wind']['Speed']['Value']

        ingame = []

        if weather == 'Partly sunny' or weather == 'Intermittent clouds' or weather == 'Partly cloudy' or weather == 'Partly sunny w/ Showers' or weather == 'Partly Cloudy w/ Showers' or weather == 'Partly sunny w/ Flurries' or weather == 'Partly sunny w/ T-Storms' or weather == 'Partly Cloudy w/ T-Storms':
            ingame = 'Partly cloudy'
        else:
            ingame = ingame
            
        if weather == 'Mostly cloudy' or weather == 'Cloudy' or weather == 'Mostly cloudy w/ showers' or weather == 'Mostly cloudy w/ T-Storms' or weather == 'Mostly cloudy w/ Flurries' or weather == 'Hazy Sunshine' or weather == 'Hazy Moonlight':
            ingame = 'Cloudy'
        else:
            ingame = ingame

        if weather == 'Sunny' or weather == 'Clear' or weather == 'Mostly sunny' or weather == 'Mostly clear':
            ingame = 'Clear'
        else:
            ingame = ingame

        if weather == 'Fog':
            ingame = 'Fog'
        else:
            ingame = ingame

        if weather == 'Showers' or weather == 'Rain' or weather == 'T-Storms':
            ingame = 'Rainy'
        else:
            ingame = ingame

        if weather == 'Rain and Snow' or weather == 'Flurries' or weather == 'Snow':
            ingame = 'Snowy'
        else:
            ingame = ingame
            
        if wind > 14.91:
            ingame = 'Windy'
        else:
            ingame = ingame
            
        forcast.extend([datetime[:10] + '\t' + datetime[11:16] + '\t' + ingame + '\t' + str(wind)])
    forcast.extend(['\nWinds above 14.9 mph will result in windy weather'])
    await bot.say('\n'.join(forcast))

token = 'NTA5Njc0NDQ5NzY3NzU4ODcy.Dsro3g.KoC7H7PSECN1PrmZKf3a5ytDV3U'
pancakes = 'NTA5Njc0NDQ5NzY3NzU5ODcy.Dtrarw.ndFwxW_xv7PjSh9OU5IJUihMF6I'
bot.run(pancakes)
