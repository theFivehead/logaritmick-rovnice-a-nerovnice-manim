
from numbers import Number


from manim import *
from manim.opengl import *

from numpy import *

from typing_extensions import runtime



class Uvod(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-5, 5, 1],
            y_length=6.5,
            tips=False,
            axis_config={"include_numbers": True},
            x_axis_config={"color": RED},
            y_axis_config = {"color": BLUE},
        )
        # x_min must be > 0 because log is undefined at 0.
        logarithms = ax.plot(lambda x: np.log(x), x_range=[1/e**5,10,0.01], use_smoothing=False)
        graf = VGroup(ax, logarithms)
        graf.scale(0.6).to_edge(DOWN)

        H1=Text("Témata:")
        popis=Text("- přehled všech vzorců pro počítání s logaritmy\n\n- ukázka rovnic či nerovnic a úprav obou jejich stran na logaritmy se stejným základem\n\n- ukázka použití substituce při řešení logaritmické rovnice či nerovnice", font_size="22")
        H1.to_edge(UP)
        popis.next_to(H1,direction=np.array((0.0, -2.0, 0.0))).to_edge(np.array((0.5, 0.0, 0.0)))

        self.play(Write(H1))
        self.play(Write(popis))
        self.play(Write(ax,run_time=5))
        self.wait(0.5)
        self.play(Create(logarithms))
        self.wait(10)
        #self.interactive_embed()
        self.play(Unwrite(H1),Unwrite(popis,run_time=3))
        self.play(Unwrite(graf,run_time=5))
        self.wait(2)


class vzorce(Scene):
    def construct(self):
        H1=Text("Vzorce:").to_edge(UL)
        logarimus=MathTex(r"\log","_a","x"," = ","y")
        log_na_cislo=MathTex(r"x"," = ","a","^y")
        log_vzorce=MathTex(
        r"\log_a(a) = 1", r"\\",
        r"\log_a(1) = 0", r"\\",
        r"a^{\log_a(x)} = \log_a(a^x) = x", r"\\",
        r"\log_b(a) \cdot \log_a(b) = 1", r"\\",
        r"\log_a(x^r) = r \log_a(x)", r"\\",
        r"\log_a(b \cdot c) = \log_a(b) + \log_a(c)", r"\\",
        r"\log_a\left(\frac{b}{c}\right) = \log_a(b) - \log_a(c)",font_size=50
        )
        prigozin=ImageMobject("Yevgeny-Prigozhin-Pointing-meme-7lavbl.png")
        sipka_prevodu=Arrow(1 * UP, 0.5 * DOWN)
        ln_vzorce = MathTex(r"\ln(x) = \log_e(x), \quad \ln(e) = 1")
        euler_vzorec=MathTex(r"e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n")
        euler=MathTex("2,7182818284")
        #pozice
        #log
        log_vzorce.to_edge(np.array((1.0, -1.0, 0.0)))
        logarimus.to_edge(np.array((-1.0, 4.0, 0.0)))
        sipka_prevodu.next_to(logarimus,DOWN)
        log_na_cislo.next_to(sipka_prevodu,DOWN)
        prigozin.next_to(sipka_prevodu, np.array((0.001, 0.0, 0.0)))
        #ln-----------------------------------
        ln_vzorce.to_edge(np.array((0.0, 4.0, 0.0)))
        euler_vzorec.next_to(ln_vzorce,DOWN)
        euler.next_to(euler_vzorec,np.array((0.0, -4.0, 0.0)))
        sipka_euler = Arrow(start=euler_vzorec.get_bottom(),end=euler.get_top())


        self.play(Write(H1))
        self.wait(3)
        self.play(Write(logarimus))
        self.wait(6)
        self.play(GrowArrow(sipka_prevodu))
        self.play(TransformFromCopy(logarimus,log_na_cislo))
        self.wait(2)
        self.play(logarimus.animate.set_color_by_tex("x",RED),log_na_cislo.animate.set_color_by_tex("x",RED))
        self.wait(0.5)
        self.play(logarimus.animate.set_color_by_tex("a", BLUE), log_na_cislo.animate.set_color_by_tex("a", BLUE))
        self.wait(0.5)
        self.play(logarimus.animate.set_color_by_tex("y", GREEN), log_na_cislo.animate.set_color_by_tex("y", GREEN))
        self.wait(1)
        self.play(FadeIn(prigozin))
        self.wait(6)
        self.play(Write(log_vzorce,run_time=5))
        self.wait(10)
        self.play(FadeOut(prigozin))
        self.play(Unwrite(VGroup(logarimus,sipka_prevodu,log_na_cislo,log_vzorce)))
        #LN vzorce dostylizovat
        self.play(Write(ln_vzorce))
        self.play(Write(euler_vzorec))
        self.wait(2)
        self.play(GrowArrow(sipka_euler))
        self.play(Write(euler))
        self.wait(5)
        self.play(Unwrite(VGroup(ln_vzorce,euler_vzorec,euler,sipka_euler)))
        self.play(Unwrite(H1))
        self.wait(2)


#ROVNICE --------------------------------------------------------------------
class rovnice1(Scene):
    def construct(self):
        scenaV=VGroup()
        zadani=MathTex(r"\log_","3","(x+4)"," = ","2").to_edge(UP)
        rovnice=MathTex(r"log_","a","x","=","y").to_edge(UR)
        rovnice_vysledek=(MathTex("x","=","a^","y")).next_to(rovnice,DOWN)

        self.play(Write(zadani))
        self.wait(5)
        self.play(TransformFromCopy(zadani,rovnice))
        self.play(TransformFromCopy(rovnice, rovnice_vysledek))
        self.play(rovnice.animate.set_color_by_tex("x",RED).set_color_by_tex("a",BLUE).set_color_by_tex("y",GREEN))
        self.play(rovnice_vysledek.animate.set_color_by_tex("x",RED).set_color_by_tex("a",BLUE).set_color_by_tex("y",GREEN))
        self.wait(2)
        self.play(zadani.animate.set_color_by_tex("x", RED).set_color_by_tex("3", BLUE).set_color_by_tex("2", GREEN))
        self.wait(2)
        steps = [
            MathTex(r"x + 4"," = ","3","^2").set_color_by_tex("3", BLUE).set_color_by_tex("2", GREEN),                         # Přechod na exponenciální tvar
            MathTex(r"x ","+ 4 = 9"),                           # Výpočet 3^2
            MathTex(r"x ","= 9 - 4"),                           # Izolace x
            MathTex(r"x ","= 5")                                # Řešení
        ]
        for i, step in enumerate(steps):
            scenaV.add(step)
            step.set_color_by_tex("x", RED)
            if i == 0:
                step.next_to(zadani,DOWN)
                self.play(TransformFromCopy(zadani, step))
            else:
                step.next_to(steps[i-1],DOWN)
                self.play(TransformFromCopy(steps[i-1], step))
            self.wait(2.5)
        podtrhnuti=VGroup(Underline(steps[len(steps) - 1],buff=0.01).next_to(steps[len(steps)-1],np.array((0.0, -0.1, 0.0))),Underline(steps[len(steps) - 1],buff=0.01).next_to(steps[len(steps)-1],np.array((0.0, -0.5, 0.0))))
        self.play(Write(podtrhnuti))
        scenaV.add(podtrhnuti)

        self.wait(3)
        self.play(Unwrite(rovnice),Unwrite(rovnice_vysledek))
        self.play(Unwrite(zadani),reverse=False)
        self.play(Unwrite(scenaV,reverse=False))
        self.wait(1)
        #self.interactive_embed()

class rovnice2(Scene):
    def construct(self):
        zadani = MathTex(r"\log_","3","(5+4 \cdot \log_2(x-1))"," ="," 2").to_edge(UP)  # Původní rovnice
        rovnice=MathTex(r"log_","a","x","=","y").to_edge(UL)
        rovnice_vysledek=MathTex("x","=","a^","y").next_to(rovnice,DOWN)
        scenaV=VGroup()
        mezi_vypocet_z=MathTex(r"x"," = ","3","^2").next_to(zadani,np.array((8.0, 0.0, 0.0))).set_color_by_tex("x", RED).set_color_by_tex("3", BLUE).set_color_by_tex("2", GREEN)
        mezi_vypocet_v=MathTex(r"x"," ="," 9").next_to(mezi_vypocet_z,DOWN).set_color_by_tex("x", RED).set_color_by_tex("9", YELLOW)
        mezi_vypocet=VGroup(mezi_vypocet_z,mezi_vypocet_v)
        rovnice.set_color_by_tex("x",RED).set_color_by_tex("a",BLUE).set_color_by_tex("y",GREEN)
        rovnice_vysledek.set_color_by_tex("x", RED).set_color_by_tex("a", BLUE).set_color_by_tex("y", GREEN)

        odvozeni=Arrow(start=zadani.get_right(),end=mezi_vypocet_z.get_left())

        self.play(Write(zadani))
        self.wait(8)
        self.play(Write(rovnice))
        self.play(Write(rovnice_vysledek))
        self.wait(5)
        self.play(zadani.animate.set_color_by_tex("3",BLUE))
        self.wait(1.5)
        self.play(zadani.animate.set_color_by_tex(" 2", GREEN))
        self.wait(0.5)
        self.play(GrowArrow(odvozeni))
        self.play(Write(mezi_vypocet))
        self.wait(2)
        steps = [
            MathTex(r"\log_3(5+4 \cdot \log_2(x-1)) = ","\log_3 ","9").set_color_by_tex("9",YELLOW),  # Logaritmický ekvivalent
            MathTex(r"5+4 \cdot \log_2(x-1) = 9"),  # Přechod na ekvivalent bez logaritmu
            MathTex(r"4 \cdot \log_2(x-1)"," ="," 4"),  # Izolace logaritmu
            MathTex(r"\log_","2","(x-1)"," = ","1").set_color_by_tex("1",GREEN).set_color_by_tex("2",BLUE).set_color_by_tex("x", RED),  # Dělení oběma stranami
            MathTex(r"x-1"," = ","2","^1").set_color_by_tex("1",GREEN).set_color_by_tex("2",BLUE).set_color_by_tex("x", RED),  # Přechod na exponenciální tvar
            MathTex(r"x = 3",substrings_to_isolate="x").set_color_by_tex("x", RED)  # Výpočet
        ]
        for i, step in enumerate(steps):
            scenaV.add(step)
            if i == 0:
                step.next_to(zadani,DOWN)
                self.play(TransformFromCopy(zadani, step))
            else:
                step.next_to(steps[i-1],DOWN)
                self.play(TransformFromCopy(steps[i-1], step))
            self.wait(2)
        podtrhnuti=VGroup(Underline(steps[len(steps) - 1],buff=0.01).next_to(steps[len(steps)-1],np.array((0.0, -0.1, 0.0))),Underline(steps[len(steps) - 1],buff=0.01).next_to(steps[len(steps)-1],np.array((0.0, -0.5, 0.0))))
        self.play(Write(podtrhnuti))
        scenaV.add(podtrhnuti)
        self.wait(5)
        self.play(Unwrite(rovnice),Unwrite(rovnice_vysledek))
        self.play(Unwrite(odvozeni))
        self.play(Unwrite(mezi_vypocet))
        self.play(Unwrite(zadani),reverse=False)
        self.play(Unwrite(scenaV), reverse=False)
        self.wait(2)

class rovnice3(Scene):
    def construct(self):
        zadani = MathTex(r"\log","(1+x)"," - \log","(1-x)"," = \log","(x+3)"," - \log","(4-x)").to_edge(UP)   # Původní rovnice
        rovnice_log_deleni = MathTex(r"\log_a\left(\frac{r}{s}\right) = \log_a(r) - \log_a(s)").next_to(zadani, np.array((0.0, -3.0, 0.0)))

        krok2=MathTex(r"\log\left(\frac{1+x}{1-x}\right) = \log\left(\frac{x+3}{4-x}\right)").next_to(rovnice_log_deleni,DOWN)

        krok2.next_to(rovnice_log_deleni, np.array((0.0, -3.0, 0.0)))
        polomer=4
        sipka1=CurvedArrow(start_point=zadani.get_corner(DL),end_point=krok2.get_left(),radius=polomer)
        sipka2=CurvedArrow(start_point=zadani.get_corner(DR),end_point=krok2.get_right(),radius=-polomer)
        sipky=VGroup(sipka2,sipka1)
        krok2[0][4:7].set_color(GREEN)
        krok2[0][17:20].set_color(GREEN)
        krok2[0][8:11].set_color(BLUE)
        krok2[0][21:24].set_color(BLUE)


        self.play(Write(zadani))
        self.wait(9)
        self.play(Write(rovnice_log_deleni))
        self.wait(7)
        self.play(zadani[1].animate.set_color(GREEN),
                  zadani[3].animate.set_color(BLUE),
                  zadani[5].animate.set_color(GREEN),
                  zadani[7].animate.set_color(BLUE),

                  )

        self.play(rovnice_log_deleni[0][5:6].animate.set_color(GREEN),
                  rovnice_log_deleni[0][15:16].animate.set_color(GREEN),
                  rovnice_log_deleni[0][7:8].animate.set_color(BLUE),
                  rovnice_log_deleni[0][23:24].animate.set_color(BLUE),
                  )
        self.wait(3)
        self.play(Write(sipky[0]),Write(sipky[1]))
        self.wait(2)
        self.play(Write(krok2))
        self.wait(2)
        self.play(Unwrite(rovnice_log_deleni))
        self.play(Unwrite(sipky))
        self.play(krok2.animate.next_to(zadani,DOWN))

        scenaV = VGroup(zadani,krok2)

        steps = [
            # Použití pravidla pro rozdíl logaritmů
            MathTex(r"\frac{1+x}{1-x} = \frac{x+3}{4-x}"),  # Initial equation after removing logs
            MathTex(r"(1+x)(4-x) = (1-x)(x+3)", tex_to_color_map={"x": RED}),  # Cross multiplication
            MathTex(r"4 - x + 4x - x^2 = x + 3 - x^2 - 3x", tex_to_color_map={"x": RED}),  # Expand the terms
            MathTex(r"4 + 3x - x^2 = 3 - 3x - x^2", tex_to_color_map={"x": RED}),  # Rearrange terms
            MathTex(r"6x = -1", tex_to_color_map={"x": RED}),  # Isolate variable x
            MathTex(r"x = -\frac{1}{6}", tex_to_color_map={"x": RED})  # Final result
        ]
        for i, step in enumerate(steps):
            scenaV.add(step)
            if i == 0:
                step.next_to(krok2,DOWN)
                step[0][2:3].set_color(RED)
                step[0][6:7].set_color(RED)
                step[0][10:11].set_color(RED)
                step[0][14:15].set_color(RED)
                self.play(TransformFromCopy(krok2, step))
            else:
                step.next_to(steps[i-1],DOWN)
                self.play(TransformFromCopy(steps[i-1], step))
            self.wait(2.5)
        podtrhnuti=VGroup(Underline(steps[len(steps) - 1],buff=0.01).next_to(steps[len(steps)-1],np.array((0.0, -0.1, 0.0))),Underline(steps[len(steps) - 1],buff=0.01).next_to(steps[len(steps)-1],np.array((0.0, -0.5, 0.0))))
        self.play(Write(podtrhnuti))
        scenaV.add(podtrhnuti)
        self.wait(5)
        self.play(Unwrite(scenaV,reverse=False,run_time=3))
        self.wait(2)
#NEROVNICE --------------------------------------------------------------------
class nerovnice1(Scene):
    def construct(self):

        zadani = MathTex(r"\log_","5","(3x - 1)"," < ","3")
        def_obor=VGroup(MathTex("x>0",substrings_to_isolate="x"),MathTex(r"3x - 1 > 0",substrings_to_isolate="x"),MathTex(r"3x > 1",substrings_to_isolate="x"),MathTex(r"x > \frac{1}{3}",substrings_to_isolate="x"))
        def_obor.arrange(DOWN)
        rovnice=MathTex(r"log_","a","x","=","y").to_edge(UL).set_color_by_tex("x",RED).set_color_by_tex("a",BLUE).set_color_by_tex("y",GREEN)
        rovnice_vysledek=(MathTex("x","=","a^","y")).next_to(rovnice,DOWN).set_color_by_tex("x",RED).set_color_by_tex("a",BLUE).set_color_by_tex("y",GREEN)

        for i in def_obor:
            i.set_color_by_tex("x",RED_B)

        zadani.to_edge(UP).set_color_by_tex("5",BLUE).set_color_by_tex("3",GREEN).set_color_by_tex("3x",RED)
        scenaV = VGroup(zadani)
        def_obor.to_edge(UR)
        self.play(Write(zadani))
        self.wait(10)
        self.play(Write(def_obor[0]))
        sipka1 = CurvedArrow(start_point=zadani[2].get_corner(DOWN), end_point=def_obor[1].get_left(), radius=5)
        self.play(Write(sipka1))
        self.play(Write(def_obor[1]))
        self.wait(2)
        self.play(Unwrite(sipka1))
        self.play(Write(def_obor[2:],run_time=2))
        self.wait(3)
        self.play(Write(rovnice))
        self.play(Write(rovnice_vysledek))

        steps=[
            MathTex(r"3x - 1"," < ","5","^3").set_color_by_tex("5",BLUE).set_color_by_tex("3",GREEN).set_color_by_tex("3x",RED),
            MathTex(r"3x - 1 < 125",substrings_to_isolate="x"),
            MathTex(r"3x < 126",substrings_to_isolate="x"),
            MathTex(r"x < 42",substrings_to_isolate="x")
        ]
        for i, step in enumerate(steps):
            scenaV.add(step)
            if i == 0:
                step.next_to(zadani, DOWN)
                self.play(TransformFromCopy(zadani, step))
            else:
                step.set_color_by_tex("x",RED)
                step.next_to(steps[i-1],DOWN)
                self.play(TransformFromCopy(steps[i-1], step))
            self.wait(2.5)

        self.play(Unwrite(rovnice))
        self.play(Unwrite(rovnice_vysledek))

        self.play(scenaV.animate.to_edge(LEFT))


        osa = NumberLine(x_range=[0,45,5],include_tip=False,length=8,numbers_to_include=[1/3,42],decimal_number_config={"num_decimal_places": 1})
        osa.to_edge(DOWN)

        interval=MathTex(r"\left(\frac{1}{3}; 42\right)")

        pozice1 = osa.number_to_point(1.0/3.0)
        pozice2 = osa.number_to_point(42)
        konec1=osa.number_to_point(45) + UP
        konec2=osa.number_to_point(0) + UP*1/2


        prunik1=VGroup(Line(start=pozice1,end=pozice1 + UP,color=RED_B),
                       Line(start=pozice1 + UP,end=konec1,color=RED_B),
                       ArrowTriangleFilledTip(start_angle=0,color=RED_B).move_to(konec1),
                       Circle(color=RED_B, radius=0.1).move_to(pozice1 + UP)
                       )

        prunik2 = VGroup(Line(start=pozice2, end=pozice2 + UP*1/2,color=RED),
                         Line(start=pozice2 + UP*1/2, end=konec2,color=RED),
                         ArrowTriangleFilledTip(color=RED).move_to(konec2),
                         Circle(color=RED, radius=0.1).move_to(pozice2 + UP*1/2)
                         )

        prurez=Rectangle(width=pozice2[0]-pozice1[0],height=1,color=ORANGE).move_to(pozice1,DL)

        interval.next_to(prurez).shift(np.array((1.3, 0.0, 0.0)))
        self.play(Write(osa))
        self.wait(1)
        self.play(Write(prunik1))
        self.wait(2)
        self.play(Write(prunik2))
        self.wait(3)
        self.play(FadeIn(prurez))
        self.play(prurez.animate.set_opacity(0.5))
        self.play(Write(interval))
        self.wait(6)
        #konec sceny-------------------------
        self.play(Unwrite(scenaV,reverse=False))
        self.play(Unwrite(def_obor,reverse=False))
        self.play(Unwrite(prurez))
        self.play(Unwrite(prunik1),Unwrite(prunik2))
        self.play(Unwrite(osa))
        self.wait(1)
        self.play(Unwrite(interval))
        self.wait(2)

class nerovnice2(Scene):
    def construct(self):
        barva_rovnice = YELLOW_D
        barva_y=YELLOW_C
        zadani = MathTex(r"\log","^2","_{0.5}x"," + ","\log_{0.5}x"," - 2 \leq 0").to_edge(UP)
        zadani_krok1=MathTex(r"(\log_{0.5}x)","^2 + ","\log_{0.5}x"," - 2 \leq 0").set_color_by_tex("log",barva_rovnice)
        substituce=MathTex(r"y ","="," \log_{0.5}x").to_edge(UR)
        substituce_zadani=MathTex(r"y^2"," + ","y"," - 2 \leq 0",substrings_to_isolate="y").move_to(zadani).set_color_by_tex("y",barva_y)
        otaceni_znamenka=MathTex(r"0 < ","a"," < 1",color=ORANGE).set_color_by_tex("a",TEAL)



        D=MathTex(r"D = 1^2 - 4 \cdot 1 \cdot (-2) = 9").next_to(substituce_zadani,DOWN)
        kvadRov=MathTex(r"y_{1,2} = \frac{-1 \pm \sqrt{9}}{2 \cdot 1} = \frac{-1 \pm 3}{2} = ").next_to(D,DOWN)
        kvadRov[0][0:4].set_color(barva_y)

        y12=VGroup(MathTex(r"y_1"," {{=}} 1"),MathTex(r"y_2"," {{=}} -2"))
        ny12=VGroup(MathTex(r"y_1"," {{\leq}} 1",tex_to_color_map={"y_1":YELLOW}),MathTex(r"y_2"," {{\geq}} -2",tex_to_color_map={"y_2":YELLOW}))
        n1=VGroup(MathTex(r"\log_{0.5}(x) \geq ","-2",substrings_to_isolate="x",tex_to_color_map={"0.5":TEAL}).set_color_by_tex("-2",barva_y),MathTex(r"x \leq (0.5)^{-2}",substrings_to_isolate="x",tex_to_color_map={"0.5":TEAL,"-2":YELLOW}),MathTex(r"x \leq 4",substrings_to_isolate="x"))
        n2=VGroup(MathTex(r"\log_{0.5}(x) \leq ","1",substrings_to_isolate="x",tex_to_color_map={"0.5":TEAL}).set_color_by_tex("1",barva_y),MathTex(r"x \geq (0.5)^1",substrings_to_isolate="x",tex_to_color_map={"0.5":TEAL,"1":YELLOW}),MathTex(r"x \geq 0.5",substrings_to_isolate="x"))

        for i in n1:
            i.set_color_by_tex("x", RED_D)
        for i in n2:
            i.set_color_by_tex("x", RED_B)

        y12.arrange(DOWN, aligned_edge=LEFT).shift(RIGHT).next_to(kvadRov).shift(RIGHT)
        for i in y12:
            i.set_color_by_tex("y",barva_y)

        substituce_zadani.next_to(zadani,np.array((0.0, 0.0, 0.0)))
        zadani_krok1.next_to(zadani,np.array((0.0, 0.0, 0.0)))
        sipky=VGroup(Arrow(start=kvadRov.get_right(),end=y12[0].get_left()),Arrow(start=kvadRov.get_right(),end=y12[1].get_left()))


        self.play(Write(zadani))
        self.wait(12)
        self.play(Write(substituce))
        self.wait(1)
        self.play(substituce.animate.set_color_by_tex("y",barva_rovnice),substituce[0].animate.set_color(barva_y))
        self.play(zadani[0].animate.set_color(barva_rovnice),zadani[2].animate.set_color(barva_rovnice),zadani[4].animate.set_color(barva_rovnice))
        self.wait(3)

        self.play(TransformMatchingTex(zadani,zadani_krok1))
        self.wait(3)
        self.play(TransformMatchingTex(zadani_krok1,substituce_zadani))

        #reseni kvadraticke nerovnice
        self.wait(4)
        self.play(Write(D))
        self.play(Write(kvadRov,run_time=2))

        for i in range(2):
            self.play(GrowArrow(sipky[i]))
            self.play(Write(y12[i]))
        self.wait(2)
        self.play(Unwrite(D))
        self.play(Unwrite(kvadRov),Unwrite(sipky))
        self.play(y12[1].animate.to_edge(np.array((-3.0, 3.0, 0.0))),y12[0].animate.to_edge(np.array((3.0, 3.0, 0.0))))
        self.wait(2)
        kvad_osa=NumberLine(x_range=[-4,4,1])
        parabola= lambda x: x**2 + x - 2
        graf_parabola=FunctionGraph(parabola, x_range=[-3, 2],color=MAROON)
        vypln=Square(5,fill_opacity=0.8,fill_color=ORANGE)
        kvadraicka_funkce=VGroup(Line(kvad_osa.get_right(),kvad_osa.get_left()),kvad_osa,graf_parabola)
        kvadraicka_funkce.to_edge(DOWN)
        vypln.align_to(kvadraicka_funkce[0],UP)
        kvad_osa.add_numbers([-2,1,0])
        vypln=Intersection(graf_parabola,vypln,color=ORANGE, fill_opacity=0.6)
        kvad_sipky=VGroup(Arrow(start=LEFT,end=RIGHT*2),Arrow(start=RIGHT,end=LEFT*2))

        kvad_sipky.next_to(kvad_osa,DOWN * 2)
        kvad_sipky[0].align_to(kvad_osa.number_to_point(-2),LEFT).shift(LEFT*2.5)
        kvad_sipky[1].align_to(kvad_osa.number_to_point(1),RIGHT).shift(RIGHT*2.5)

        self.play(Write(kvad_osa))
        self.play(Create(graf_parabola))
        self.wait(5)
        self.play(FadeIn(vypln))
        self.wait(3)
        self.play(GrowArrow(kvad_sipky[0]),GrowArrow(kvad_sipky[1]))
        self.wait(5)


        ny12[0].move_to(y12[0])
        ny12[1].move_to(y12[1])
        self.play(TransformMatchingTex(y12[0],ny12[0],runtime=1))
        self.wait(1)
        self.play(TransformMatchingTex(y12[1], ny12[1],runtime=1))
        self.wait(1)
        self.play(FadeOut(vypln))
        self.play(Unwrite(kvad_sipky))
        self.play(Uncreate(graf_parabola),Unwrite(kvad_osa))
        self.wait(1)

        n1.arrange(DOWN).next_to(y12[1],DOWN)
        n2.arrange(DOWN).next_to(y12[0],DOWN)
        otaceni_znamenka.to_edge(np.array((0.0, 3.0, 0.0)))


        self.wait(1)
        self.play(ApplyWave(substituce))
        self.play(Write(n1[0]))
        self.wait(2)
        self.play(Write(n2[0]))
        self.wait(2)
        self.play(Unwrite(substituce))
        self.play(Write(otaceni_znamenka))
        self.wait(12)
        self.play(Write(n1[1:],run_time=4))
        self.play(Write(n2[1:],run_time=4))
        self.play(Unwrite(otaceni_znamenka))
        #pridani osy pruniku---------------------------------------------------------------------------------------------------------
        osa = NumberLine(x_range=[0, 5, 1], include_tip=False, length=8, numbers_to_include=[1/2, 4],
                         decimal_number_config={"num_decimal_places": 1})
        osa.to_edge(DOWN)

        interval = MathTex(r"\left<\frac{1}{2}, 4\right>")

        pozice1 = osa.number_to_point(1.0 / 2.0)
        pozice2 = osa.number_to_point(4) #dodelat--------------------------------------------------------------------------------------------------------
        konec1 = osa.number_to_point(5) + UP
        konec2 = osa.number_to_point(0) + UP * 1 / 2

        prunik1 = VGroup(Line(start=pozice1, end=pozice1 + UP,color=RED_B),
                         Line(start=pozice1 + UP, end=konec1,color=RED_B),
                         ArrowTriangleFilledTip(start_angle=0, color=RED_B).move_to(konec1),
                         Circle(color=RED_B, radius=0.1,fill_color=RED_B,fill_opacity=1).move_to(pozice1 + UP)
                         )

        prunik2 = VGroup(Line(start=pozice2, end=pozice2 + UP * 1 / 2,color=RED_D),
                         Line(start=pozice2 + UP * 1 / 2, end=konec2,color=RED_D),
                         ArrowTriangleFilledTip(color=RED_D).move_to(konec2),
                         Circle(color=RED_D, radius=0.1,fill_color=RED_D,fill_opacity=1).move_to(pozice2 + UP * 1 / 2)
                         )

        prurez = Rectangle(width=pozice2[0] - pozice1[0], height=1, color=ORANGE).move_to(pozice1, DL)

        interval.next_to(prurez).shift(np.array((2.2, 0.0, 0.0)))

        self.play(Write(osa))
        self.wait(1)
        self.play(Write(prunik1))
        self.wait(2)
        self.play(Write(prunik2))
        self.wait(3)
        self.play(FadeIn(prurez))
        self.play(prurez.animate.set_opacity(0.5))
        self.wait(2)
        self.play(Write(interval))
        self.wait(5)
        #vymazani sceny
        self.play(Unwrite(substituce_zadani))
        self.play(Unwrite(VGroup(ny12,n1,n2),reverse=False))
        self.play(Unwrite(prurez))
        self.play(Unwrite(prunik1),Unwrite(prunik2))
        self.play(Unwrite(osa))
        self.wait(2)
        self.play(Unwrite(interval))
        self.wait(2)


class vsechno(Scene):
    def construct(self):
        Uvod.construct(self)
        vzorce.construct(self)
        rovnice1.construct(self)
        rovnice2.construct(self)
        rovnice3.construct(self)
        nerovnice1.construct(self)
        nerovnice2.construct(self)