
#j'aimerai traduire les commentaires en anglais
#I would like to translate the comments into English

#mon objectif est de creer un script qui permet d'envoyer des messages sur snapchat web à partir de python et de selenium
#my goal is to create a script that allows you to send messages on snapchat web from python and selenium

#j'utilise selenium car il permet de simuler un utilisateur humain et de naviguer sur le web
#I use selenium because it allows you to simulate a human user and navigate the web

import pyautogui
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import os 
import time
import pyperclip




class SnapchatBot():
    
    def __init__(self,first_connection=False):
        self.previous_target = ""
        options = uc.ChromeOptions()
        options.user_data_dir = "c:\\profile"
        self.driver = uc.Chrome(options=options)
        #on se connecte sur snapchat web
        self.driver.get('https://web.snapchat.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(100)
        time.sleep(2)
        if first_connection:
            #mettre le programme en attente pour que l'utilisateur puisse se connecter
            #put the program on hold so that the user can connect
            input("Connectez vous sur snapchat web puis appuyez sur entrée")
        #la première fois qu'on se connecte, l'utilisateur doit renseigner ses identifiants de connexion
        #the first time we connect, the user must enter their login details



    def chat_click(self):
        self.driver.find_element(by=By.XPATH, value="/html/body/main/div[1]/div[2]/div").click()

    def send_message(self, message,target, group):
        self.join_conversation(target, group)
        time.sleep(2)
        self.write_message(message)
        self.submit()

    def write_message(self, message):
        self.driver.find_element(by=By.XPATH, value="/html/body/main/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div").send_keys(message)
    def submit(self):
        self.driver.find_element(by=By.XPATH, value="/html/body/main/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/button").click()
    def send_message_to_all(self,message):
        #envoi un message à tous les amis et groupes
        #send a message to all friends and groups
        for friend in self.friends_list:
            self.send_message(message,friend, False)
        for group in self.groups_list:
            self.send_message(message,group, True)

    
    def get_text(self):
        self.chat_click()
        #cliquer gauche sur le milieu de la page avec le module pyautogui en utilisant les coordonnées de la page
        #left click in the middle of the page with the pyautogui module using the page coordinates
        pyautogui.click(pyautogui.size()[0]/2,pyautogui.size()[1]/2)
        #faire un ctrl + a gauche avec le module pyautogui
        #do a ctrl + a left with the pyautogui module
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        #faire un ctrl + c avec le module pyautogui
        #do a ctrl + c with the pyautogui module
        pyautogui.hotkey('ctrl', 'c')
        #enregistrer le presse papier dans une variable aevc le module pyperclip
        #save the clipboard in a variable with the pyperclip module
        return pyperclip.paste()

            
    def open_friendsgroups_list(self):

        self.driver.find_element(by=By.XPATH,value="/html/body/main/div[1]/div[1]/div[1]/div[3]/button").click()
        
        self.friends_list = {self.driver.find_elements(by=By.CLASS_NAME, value='PqRmI')[i].text: element for i, element in enumerate(self.driver.find_elements(by=By.CLASS_NAME, value='PqRmI'))}

        self.groups_list={}
        for i,element in enumerate(self.driver.find_elements(by=By.CLASS_NAME, value='RbA83')):

            
            if len(element.find_elements(by=By.TAG_NAME, value='span')) == 2:
                self.groups_list[element.text] = element

            else:                    
                self.groups_list[f"no_group_name_{i}"] = element
                #le nom du groupe n'est pas fixe, je lui donne un nom en fonction de sa position dans la liste
                #the group name is not fixed, I give it a name according to its position in the list



    def stop(self):
        time.sleep(2)
        self.driver.close()



    def close_friendsgroups_list(self):
        self.driver.find_element(by=By.XPATH,value="/html/body/main/div[1]/div[2]/div/div[2]/div/form/div[1]/button").click()

    def join_conversation(self, target, group):
        #si group est à True, alors on cherche dans la liste des groupes
        #if group is True, then we look in the list of groups
        #sinon on cherche dans la liste des amis
        #otherwise we look in the list of friends
        if target!=self.previous_target:
            self.open_friendsgroups_list()
            self.driver.find_element(by=By.XPATH,value="/html/body/main/div[1]/div[1]/div[1]/div[3]/button").click()
            if group:
                print(self.groups_list[target])
                self.groups_list[target].click()
            else:
                self.friends_list[target].click()
            #confirmer le choix
            #confirm the choice
            self.driver.find_element(by=By.XPATH,value="/html/body/main/div[1]/div[2]/div/div[2]/div/form/div[5]/button[1]").click()
        self.chat_click()
        self.previous_target = target


    def get_group_members(self,group_name):
        self.open_friendsgroups_list()
        self.close_friendsgroups_list()
        if group_name in self.groups_list.keys():
            self.join_conversation(group_name, group=True)
        else:
            return Exception("This group doesn't exist")

        self.driver.find_element(by=By.XPATH,value="/html/body/main/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div[2]/span/span").click()
        self.driver.find_element(by=By.XPATH,value="/html/body/main/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/div[4]").click()

        members=[self.driver.find_elements(by=By.CLASS_NAME, value='ouMhp')[i].text for i in range(len(self.driver.find_elements(by=By.CLASS_NAME, value='ouMhp')))]
        self.driver.find_element(by=By.XPATH,value="/html/body/main/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div[2]/span/span").click()
        return members


    def get_friends_list(self):
        self.open_friendsgroups_list()
        self.close_friendsgroups_list()
        return self.friends_list.keys()

    def get_groups_list(self):
        self.open_friendsgroups_list()
        self.close_friendsgroups_list()
        return self.groups_list.keys()


