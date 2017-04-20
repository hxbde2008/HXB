#!/usr/bin/python
# -*- coding: UTF-8 -*-

var webdriver = require('selenium-webdriver'),
    chrome = require('selenium-webdriver/chrome');

var o = new chrome.Options();
o.addExtensions(['extensions/chrome/chrome_extension.zip']); // crx file is just a zip file
var s = new chrome.ServiceBuilder('bin/chromedriver').build();
var driver = chrome.createDriver(o, s)
