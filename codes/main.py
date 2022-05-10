# CBSE Probability Grade 12
# Example 11

# Name: Velma Dhatri Reddy
# Roll number: AI21BTECH11030

""" Problem Statement
Of the students in a college, it is known that 60% reside in hostel and 40% are day scholars 
(not residing in hostel). Previous year results report that 30% of all students who reside in 
hostel attain A grade and 20% of day scholars attain A grade in their annual examination. At 
the end of the year, one student is chosen at random from the college and he has an A grade, 
what is the probability that the student is a hostler?
"""


def main():
    P_H = 0.6  # Probability that student is a hostler
    P_D = 0.4  # Probability that student is a day scholar 
    P_AH = 0.3  # Probability that that student gets A grade if a hostler 
    P_AD = 0.2  # Probability that that student gets A grade if a day scholar

    #Output
    print(f"The probability that student is a hostler if he gets an A grade is {Prob(P_H,P_D,P_AH,P_AD)}")

         
def Prob(h,d,ah,ad) -> float:
        """ Returns the probability that student is a hostler if he gets an A grade """
        return h*ah/(h*ah + d*ad)

if __name__ == '__main__':
       main()
