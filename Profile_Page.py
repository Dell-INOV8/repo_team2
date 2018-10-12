
class profileHolder(object):
    def __init__(self, nameofguy, location, dateofbirth, jobtitle, email, password, bio, skills, skillsEndoresed):
        self.nameofguy = "nameholder"
        self.location = "location"
        self.dateofbirth= "DOB"
        self.jobtitle = "job"
        self.email = "emailAddress"
        self.password = "password"
        self.bio = "person description"
        self.skills = []
        self.skillsEndoresed = []

def entername(profileHolder):
    profileHolder.nameofguy = input("please enter your name")

def readname(profileHolder):
    print(profileHolder.nameofguy)

def enterlocation(profileHolder):
    profileHolder.location = input("Please enter where you are located")

def getlocation(profileHolder):
    print(profileHolder.location)

def enterDateOfBirth(profileHolder):
    profileHolder.dateofbirth = input("Please enter your date of birth")

def getDateOfBirth(profileHolder):
    print(profileHolder.dateofbirth)

def enterJobTitle(profileHolder):
    profileHolder.jobtitle = input("Please enter your Job Title")

def getJobTitle(profileHolder):
    print(profileHolder.jobtitle)

def enterEmail(profileHolder):
    profileHolder.email = input("Please enter your email address")

def getEmail(profileHolder):
    print(profileHolder)

def enterPassword(profileHolder):
    profileHolder.password = input("Please enter your password")

def getPassword(profileHolder):
    print(profileHolder.password)

def enterBio(profileHolder):
    profileHolder.bio = input("Please enter a short bio")

def getBio(profileHolder):
    print(profileHolder.bio)

def enterSkills(profileHolder):
    numSkills = 0
    skills = []
    numSkills = input("Please enter the number of skills you wish to add")

    for x in range (0, numSkills):
        skills.append(input("enter skill " + x))

    profileHolder.skills = skills

def getSkills(profileHolder):
    print(profileHolder.skills)

def enterEndoresedSkills(profileHolder):
    skillsEndorsed = []
    currentSkills = profileHolder.skills

    print(currentSkills)
    numSkillsToEndorse = input("Please enter the skills from above you wish to endorse")

    for x in range(0,numSkillsToEndorse):
        skillsEndorsed.append(input("skill " + x + " to endorse"))

    profileHolder.skillsEndoresed = skillsEndorsed

def getEndorsedSkills(profileHolder):
    print(profileHolder.skillsEndoresed)

def createProfile(profileList):

    NumProf = len(profileList)
    

    profileHolder.nameofguy = input("please enter your name")
    profileHolder.location = input("Please enter where you are located")
    profileHolder.dateofbirth = input("Please enter your date of birth")
    profileHolder.jobtitle = input("Please enter your Job Title")
    profileHolder.email = input("Please enter your email address")


def main():

    profileList = []
    instance1 = profileHolder("joe", "someplace", "1AD", "The CEO GUY", "thatemailthing", "1234", "I am a fantastic bossman", ["sleeping", "Jaywalking", "living"], ["sleeping"])
    instance2 = profileHolder("1", "middleEarth", "now", "ringGuy", "postalBird1", "ruleThemAll", "I walk far", ["running away", "having no char development"], ["having now char development"])

    profileList.append(instance1)
    profileList.append(instance2)

main()






