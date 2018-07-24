import rectangle
import surface

def main():
    surf = surface.surface('surface_1',0,0,10,10)
    rect = surf.getRect()
    print(rect)
main()
