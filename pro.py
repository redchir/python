#!/usr/bin/env python
# -*- coding: utf-8  -*-
# gazette_date.py

try:
         import scribus
except ImportError:
         print "Unable to import the 'scribus' module. This script will only run within"
              print "the Python interpreter embedded in Scribus. Try Script->Execute Script."
                   sys.exit(1)

                   from datetime import date

                   if not scribus.haveDoc():
                            scribus.messageBox('Scribus - Script Error', "No document open", scribus.ICON_WARNING, scribus.BUTTON_OK)
                                 sys.exit(1)

                                 if scribus.selectionCount() == 0:
                                          scribus.messageBox('Scribus - Script Error',
                                                               "There is no object selected.\nPlease select a text frame and try again.",
                                                                            scribus.ICON_WARNING, scribus.BUTTON_OK)
                                               sys.exit(2)
                                               if scribus.selectionCount() > 1:
                                                        scribus.messageBox('Scribus - Script Error',
                                                                             "You have more than one object selected.\nPlease select one text frame and try again.",
                                                                                          scribus.ICON_WARNING, scribus.BUTTON_OK)
                                                             sys.exit(2)
                                                             textbox = scribus.getSelectedObject()
                                                             ftype = scribus.getObjectType(textbox)

                                                             if (ftype != "TextFrame"):
                                                                      scribus.messageBox('Scribus - Script Error', "This is not a textframe. Try again.", scribus.ICON_WARNING, scribus.BUTTON_OK)
                                                                           sys.exit(2)

                                                                           today = date.today()
                                                                           d = today.strftime("%A, %B %d, %Y")
                                                                           length = scribus.getTextLength()
                                                                           scribus.selectText(19, length-19, textbox)
                                                                           scribus.deleteText(textbox)
                                                                           scribus.insertText(d, -1, textbox)

                                                                           length = scribus.getTextLength()
                                                                           scribus.selectText(19, length-19, textbox)
                                                                           scribus.setFontSize(14.0, textbox)i
