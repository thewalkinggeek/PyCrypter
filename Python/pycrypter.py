
 ###############################################################
## PyCrypter - A File Encryption Utility                       ##
##                                                             ##
## Dependencies: wxpython, pywinstyles(optional), cryptography ##
##                                                             ##
## Written by Jon Schoenberger                                 ## 
 ###############################################################

import wx
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

# Create Main GUI
class frameMain ( wx.Frame ):

    def __init__( self ):
        wx.Frame.__init__ ( self, None, id = wx.ID_ANY, title = u"PyCrypter -A File Encryption Utility", pos = wx.DefaultPosition, size = wx.Size( 450,180 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizerFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panelMain.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_panelMain.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizerPanel = wx.BoxSizer( wx.VERTICAL )

        bSizerPanelMain = wx.BoxSizer( wx.VERTICAL )

        bSizerFile = wx.BoxSizer( wx.VERTICAL )

        bSizerFileHor = wx.BoxSizer( wx.HORIZONTAL )

        sbSizerFilePick = wx.StaticBoxSizer( wx.StaticBox( self.m_panelMain, wx.ID_ANY, u" Select File " ), wx.HORIZONTAL )

        self.m_bitmapLogo = wx.StaticBitmap( sbSizerFilePick.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"pycrypter.ico", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizerFilePick.Add( self.m_bitmapLogo, 0, wx.ALL, 5 )

        self.m_fileBrowser = wx.FilePickerCtrl( sbSizerFilePick.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        self.m_fileBrowser.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_fileBrowser.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        sbSizerFilePick.Add( self.m_fileBrowser, 1, wx.ALL|wx.EXPAND, 0 )


        bSizerFileHor.Add( sbSizerFilePick, 1, wx.EXPAND, 5 )


        bSizerFile.Add( bSizerFileHor, 0, wx.ALL|wx.EXPAND, 0 )


        bSizerPanelMain.Add( bSizerFile, 0, wx.EXPAND, 0 )

        bSizerSplit = wx.BoxSizer( wx.VERTICAL )

        bSizerSplitHor = wx.BoxSizer( wx.HORIZONTAL )

        bSizerEncrypt = wx.BoxSizer( wx.HORIZONTAL )

        bSizerButtons = wx.BoxSizer( wx.HORIZONTAL )

        self.m_buttonEncrypt = wx.Button( self.m_panelMain, wx.ID_ANY, u"Encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonEncrypt.SetLabelMarkup( u"Encrypt" )
        self.m_buttonEncrypt.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
        self.m_buttonEncrypt.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizerButtons.Add( self.m_buttonEncrypt, 0, wx.ALL, 10 )


        bSizerEncrypt.Add( bSizerButtons, 0, wx.EXPAND, 0 )


        bSizerSplitHor.Add( bSizerEncrypt, 1, wx.EXPAND, 0 )

        bSizerDecrypt = wx.BoxSizer( wx.HORIZONTAL )

        bSizerBtnD = wx.BoxSizer( wx.HORIZONTAL )

        self.m_buttonDecrypt = wx.Button( self.m_panelMain, wx.ID_ANY, u"Decrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonDecrypt.SetLabelMarkup( u"Decrypt" )
        self.m_buttonDecrypt.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
        self.m_buttonDecrypt.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizerBtnD.Add( self.m_buttonDecrypt, 0, wx.ALL, 10 )


        bSizerDecrypt.Add( bSizerBtnD, 0, wx.EXPAND, 0 )


        bSizerSplitHor.Add( bSizerDecrypt, 0, wx.EXPAND, 0 )


        bSizerSplit.Add( bSizerSplitHor, 1, wx.EXPAND, 0 )

        bSizerBottomSplit = wx.BoxSizer( wx.HORIZONTAL )

        bSizerBottom = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticAuthor = wx.StaticText( self.m_panelMain, wx.ID_ANY, u"Written by: Jon Schoenberger", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticAuthor.Wrap( -1 )

        self.m_staticAuthor.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_staticAuthor.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizerBottom.Add( self.m_staticAuthor, 1, wx.ALL, 5 )

        self.m_staticTextEnc = wx.StaticText( self.m_panelMain, wx.ID_ANY, u"128-bit AES", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextEnc.Wrap( -1 )

        self.m_staticTextEnc.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_staticTextEnc.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_staticTextEnc.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizerBottom.Add( self.m_staticTextEnc, 0, wx.ALL, 5 )


        bSizerBottomSplit.Add( bSizerBottom, 1, wx.EXPAND, 5 )


        bSizerSplit.Add( bSizerBottomSplit, 0, wx.EXPAND, 0 )


        bSizerPanelMain.Add( bSizerSplit, 1, wx.EXPAND, 0 )


        bSizerPanel.Add( bSizerPanelMain, 1, wx.EXPAND, 0 )


        self.m_panelMain.SetSizer( bSizerPanel )
        self.m_panelMain.Layout()
        bSizerPanel.Fit( self.m_panelMain )
        bSizerFrame.Add( self.m_panelMain, 1, wx.EXPAND, 0 )


        self.SetSizer( bSizerFrame )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events 
        self.m_fileBrowser.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_fileBrowserOnFileChanged )
        self.m_buttonEncrypt.Bind( wx.EVT_BUTTON, self.m_buttonEncryptOnButtonClick )
        self.m_buttonDecrypt.Bind( wx.EVT_BUTTON, self.m_buttonDecryptOnButtonClick )

        # Intialize File Path 
        self.FilePath = None

        # Populate   
        self.Show()

        # Check If Key Exists
        try:
            key_abs_path = Path('filekey.key').resolve(strict=True)
        # If Key Does Not Exist
        except FileNotFoundError:
            print("Key Was Not Found. Creating ...")
            # Generate Key
            key = Fernet.generate_key()
            # Write Key To File
            with open('filekey.key', 'wb') as filekey:
                filekey.write(key)
            print("Key Was Created!")
            # Open key
            with open('filekey.key', 'rb') as filekey:
                key = filekey.read()
            # Use Key
            fernet = Fernet(key)
        # If Key Exist
        else:
            print("Key Found!")

    # Event Handlers       
    def m_fileBrowserOnFileChanged( self, event ):
        self.FilePath = event.GetPath()
        print("Loaded File:", self.FilePath, "Successfully!")

    def m_buttonEncryptOnButtonClick( self, event ):
            # Open key
            with open('filekey.key', 'rb') as filekey:
                key = filekey.read()
            # Use Key
            fernet = Fernet(key)
            # Check If File Is Already Encrypted
            try:
                # If File Already Encrypted
                with open(self.FilePath, 'rb') as enc_file:
                    encrypted = enc_file.read()
                    fernet.decrypt(encrypted, None)
                    btnTxt = { wx.ID_OK : "OK" }
                    wx.MessageBox("File is already encrypted." % btnTxt)
                    print("File Is Already Encrypted. Ignoring ...")
            except:
                # If File is Not Already Encrypted
                # Open File
                with open(self.FilePath, 'rb') as file:
                    original = file.read()
                # Encrypt File
                encrypted = fernet.encrypt(original)
                # Open File and Write Encrypted Data
                with open(self.FilePath, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
                btnTxt = { wx.ID_OK : "OK" }
                wx.MessageBox("Encryption was a success." % btnTxt)
                print("Encryption Complete!")

    def m_buttonDecryptOnButtonClick( self, event ):
        # Open key
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        # Use Key
        fernet = Fernet(key)
        # Check If File Is Encrypted
        try:
            # If File Is Encrypted
            # Open File
            with open(self.FilePath, 'rb') as file:
                original = file.read()
            # Decrypt File
            decrypted = fernet.decrypt(original)
            # Open File and Write Decrypted Data
            with open(self.FilePath, 'wb') as dec_file:
                dec_file.write(decrypted)
            btnTxt = { wx.ID_OK : "OK" }
            wx.MessageBox("Decryption was a success." % btnTxt)
            print("Decryption Complete!")
        # If File Is Not Encrypted                   
        except InvalidToken:
            # with open(self.FilePath, 'rb') as enc_file:
            #     encrypted = enc_file.read()
            #     fernet.decrypt(encrypted, False)
            btnTxt = { wx.ID_OK : "OK" }
            wx.MessageBox("File is not encrypted." % btnTxt)
            print("File Is Not Encrypted. Ignoring ...")     

# Main Loop       
if __name__ == "__main__":
    app = wx.App(False)
    frame = frameMain()
    # Apply Theme
    frame.SetIcon(wx.Icon("pycrypter.ico"))
    app.MainLoop()
