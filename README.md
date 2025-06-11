Version 1.0.2
Created by Jarod Day

--------

This is a chrome browser extension that directly works alongside the lighthouse-automation tool that I also created. You can find the link here:
https://www.github.com/groovyjarod/lighthouse-automation

Purpose:
This extension serves to locate each error on the webpage you choose. You must first audit that webpage using the aformentioned lighthouse automation tool to get a json report detailing the errors made on the page you audited. That json report will be used by the extension tool to visually display the location of each error, along with a message detailing what the error was.

Usage:
After downloading this repository, navigate to chrome://extensions.
Once there, towards the top left corner of the window, click on the 'Load Unpacked' button.
Choose the folder you downloaded. This will create a new chrome extension that will allow you to visually see errors through the JSON report.
On any page within the wiki, or any page that was audited by the lighthouse tool, click on the extensions window in your chrome browser (should be a puzzle piece towards the top right side of your window), and click 'choose file', and then choose the file that corresponds with the webpage whose errors you would like to visually see.
Have fun!
