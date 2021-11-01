import pattern
import generator


if __name__ == '__main__':

    A = pattern.Checker(180, 30)
    b = A.draw()
    A.show()
#-------------------------------
    B=pattern.Circle(1000,100,(600,500))
    B.draw()
    B.show()
#-------------------------------
    A=pattern.Spectrum(100)
    A.draw()
    A.show()
#-------------------------------
    A = generator.ImageGenerator('data/exercise_data/', 'data/Labels.json', 5, [32, 32, 3], rotation=False, mirroring=False, shuffle=True)
    B = A.next()
    A.show(B)