from manim import *
import pandas as pd
from random import randint


def create_cross_out(vmobject, col="#ff5555", stroke_width=10):
    cross_out1 = Line(start=vmobject.get_corner(UP + LEFT),
                      end=vmobject.get_corner(DOWN + RIGHT), color=col, stroke_width=stroke_width)
    cross_out2 = Line(start=vmobject.get_corner(UP + RIGHT),
                      end=vmobject.get_corner(DOWN + LEFT), color=col, stroke_width=stroke_width)
    return VGroup(cross_out1, cross_out2)


class DT23Part1(Scene):
    def construct(self):
        self.camera.background_color = "#001014"
        # Intro
        back_square = Rectangle(height=4, width=10, color="#015e70", fill_color="#007b94", fill_opacity=0.2,
                                stroke_width=10).shift(1.5*LEFT)
        title = Paragraph("Verifying Receipt", "Transactions", font='Futura Std Medium', font_size=80, color="#fff0d5")\
            .move_to(back_square)
        title_border = SurroundingRectangle(title, color="#015e70", fill_color="#007b94", fill_opacity=0.4,
                                            buff=0.5, stroke_width=5)
        credit_text = Paragraph("Created by Ian Rundle, Jonathan Mak, and Ben Allen", "Rice Datathon 2023",
                                "Bill.com Track", font='Futura Std Medium', font_size=33, color="#fff0d5")\
            .next_to(back_square, DOWN)
        num_plane = NumberPlane(x_range=[-10, 10, 1.5], y_range=[-10, 10, 1.5],
                                background_line_style={
                                    "stroke_color": "#fff0d5",
                                    "stroke_width": 3,
                                    "stroke_opacity": 0.4
                                })
        self.play(DrawBorderThenFill(num_plane), FadeIn(back_square, shift=RIGHT), Wait(2))
        self.play(FadeIn(title_border), Write(title), Wait(2))
        self.play(DrawBorderThenFill(credit_text), Wait(2))
        self.play(FadeOut(back_square, title_border, title), FadeOut(credit_text, shift=DOWN), Wait(2))
        # Problem Statement
        problem_text = Paragraph("Receipt matching is traditionally", "tedious and prone to errors.",
                                 font='Futura Std Medium', font_size=50, color="#fff0d5").shift(2.5*UP)
        solution_text = Paragraph("However, this can be automated", "with the power of data!",
                                  font='Futura Std Medium', font_size=50, color="#fff0d5",
                                  t2c={"power of data": "#ff9955"}).shift(2.5*DOWN)
        doc_icon = ImageMobject("C:/Users/jackt/Documents/Datathon2023/Paper Icon.png").scale(0.25)
        doc_cross = create_cross_out(doc_icon, stroke_width=15)
        check_icon = ImageMobject("C:/Users/jackt/Documents/Datathon2023/Check.png").scale(0.25)
        self.play(DrawBorderThenFill(problem_text), FadeIn(doc_icon, scale=0.5), Wait(2))
        self.play(Create(doc_cross), Wait(2))
        self.play(ReplacementTransform(doc_cross, solution_text), FadeIn(check_icon, scale=0.5), Wait(2))
        # Data Available
        todo_text = Text("Data Available:", font='Futura Std Medium', font_size=70, color="#ff9955") \
            .shift(2.5 * UP + 3 * LEFT)
        self.play(ReplacementTransform(problem_text, todo_text),
                  FadeOut(solution_text, doc_icon, check_icon), Wait(2))
        line_spacer = Paragraph("1.", "2.", "3.", font='Futura Std Medium', font_size=50, color="#ff9955",
                                line_spacing=2.5).shift(6*LEFT+DOWN)
        user_data = Text("User-Reported Transactions", font='Futura Std Medium', font_size=50, color="#fff0d5")\
            .next_to(line_spacer[0], buff=0.5)
        ocr_data = Text("OCR Data", font='Futura Std Medium', font_size=50,
                        color="#fff0d5").next_to(line_spacer[1], buff=0.5)
        image_data = Text("Images of Receipts", font='Futura Std Medium', font_size=50, color="#fff0d5")\
            .next_to(line_spacer[2], buff=0.5)
        receipt_image = ImageMobject("C:/Users/jackt/Documents/Datathon2023/00d0116788763.jpg").scale(0.5)\
            .next_to(image_data).shift(2*UP+3*RIGHT)
        self.play(DrawBorderThenFill(line_spacer), Wait(2))
        self.play(FadeIn(user_data, shift=UP), Wait(1.5))
        self.play(FadeIn(ocr_data, shift=UP), Wait(1.5))
        self.play(FadeIn(image_data, shift=UP), FadeIn(receipt_image, scale=0.5), Wait(1.5))
        self.play(Unwrite(todo_text), FadeOut(line_spacer, user_data, ocr_data, image_data, receipt_image), Wait(2))
        # Summary of Results
        line_spacer2 = Paragraph("1.", "2.", "3.", font='Futura Std Medium', font_size=50, color="#ff9955",
                                 line_spacing=2).shift(6 * LEFT+0.2*DOWN)
        summary_text = Paragraph("To accomplish this, we created a pipeline", "consisting of:",
                                 font='Futura Std Medium', font_size=50, color="#fff0d5").shift(3*UP)
        text_similar = Text("Text Similarity Analysis", font='Futura Std Medium', font_size=50, color="#fff0d5")\
            .next_to(line_spacer2[0], buff=0.5)
        image_recog = Text("Image Recognition", font='Futura Std Medium', font_size=50, color="#fff0d5")\
            .next_to(line_spacer2[1], buff=0.5)
        knn_algo = Text("Gradient Descent Algorithm", font='Futura Std Medium', font_size=50, color="#fff0d5")\
            .next_to(line_spacer2[2], buff=0.5)
        accuracy_text = Text("To match receipts with over 84% accuracy!", font='Futura Std Medium', font_size=50,
                             color="#fff0d5").shift(3.2*DOWN)
        diagram_text = Text("Place_Name1", font="Times New Roman", font_size=40, color="#fff0d5").shift(4*RIGHT+0*DOWN)
        diagram_text2 = Text("Plake_Bane1", font="Times New Roman", font_size=40, color="#fff0d5").shift(4*RIGHT+1*DOWN)
        diagram_arrow = CurvedArrow(start_point=diagram_text.get_right()+0.25*RIGHT,
                                    end_point=diagram_text2.get_right()+0.25*RIGHT,
                                    color="#ff9955", angle=-0.4 * PI)
        diagram_arrow2 = CurvedArrow(start_point=diagram_text2.get_left() + 0.25 * LEFT,
                                     end_point=diagram_text.get_left() + 0.25 * LEFT,
                                     color="#ff9955", angle=-0.4 * PI)
        diagram_border = SurroundingRectangle(VGroup(diagram_arrow, diagram_arrow2, diagram_text, diagram_text2),
                                              color="#ff9955", stroke_width=7, buff=0.2, fill_color=WHITE,
                                              fill_opacity=0.1)
        self.play(Write(summary_text, run_time=1.5), DrawBorderThenFill(line_spacer2), Wait(2))
        self.play(FadeIn(text_similar, shift=UP), DrawBorderThenFill(diagram_text, run_time=1), Write(diagram_text2),
                  Create(diagram_arrow), Create(diagram_border), Create(diagram_arrow2), Wait(2))
        self.play(FadeIn(image_recog, shift=UP), Wait(1.5))
        self.play(FadeIn(knn_algo, shift=UP), Wait(1.5))
        self.play(FadeIn(accuracy_text, shift=UP), Wait(1.5))
        self.play(FadeOut(summary_text, line_spacer2, text_similar, diagram_text, diagram_text2, diagram_arrow,
                          diagram_arrow2, diagram_border, image_recog, knn_algo, accuracy_text, shift=DOWN), Wait(2))
        # EDA
        hist_data = pd.read_csv("C:/Users/jackt/Documents/GitHub/BillDatathon2023/hist_height.csv")
        axes = Axes(x_range=[0, 200, 25], y_range=[0, 150, 20],
                    x_length=10, y_length=5,
                    axis_config={"include_tip": True, "numbers_to_exclude": [0]}
                    ).add_coordinates().set_color("#fff0d5").shift(0.5 * DOWN)
        axis_labels = axes.get_axis_labels(x_label="\\$", y_label="\\#").shift(0.5*DOWN)
        axis_labels.set_color("#fff0d5")
        bar_graph = BarChart(values=hist_data.iloc[:, 1].tolist(), bar_names=[*range(0, 201, 13)], bar_width=0.9,
                             y_range=[0, 150, 10], y_length=5, x_length=10,
                             axis_config={"font_size": 30, "color": "#fff0d5"}).shift(0.5*DOWN)
        hist_title = Text("Distribution of Transactions Amounts", font='Futura Std Medium', font_size=50,
                          color="#fff0d5").shift(3*UP)
        for tick in bar_graph.get_x_axis():
            tick.set_color("#fff0d5")
        for tick in bar_graph.get_y_axis():
            tick.set_color("#fff0d5")
        self.play(DrawBorderThenFill(bar_graph), DrawBorderThenFill(axis_labels), Write(hist_title), Wait(3))
        # EDA 2
        per_data = pd.read_csv("C:/Users/jackt/Documents/GitHub/BillDatathon2023/per_height.csv")
        per_axes = Axes(x_range=[0, 61, 10], y_range=[0, 50, 51],
                        x_length=10, y_length=5,
                        axis_config={"include_tip": True, "numbers_to_exclude": [0]}
                        ).add_coordinates().set_color("#fff0d5").shift(0.5 * DOWN)
        per_axis_labels = axes.get_axis_labels(x_label="Vendors", y_label="\\#").shift(0.5 * DOWN)
        per_axis_labels.set_color("#fff0d5")
        per_graph = BarChart(values=per_data.iloc[:, 1].tolist(), bar_width=0.7,
                             y_range=[0, 61, 10], y_length=5, x_length=10, bar_colors=[RED, BLUE],
                             axis_config={"font_size": 30, "color": "#fff0d5"}).shift(0.5 * DOWN)
        per_title = Text("Number of Transactions per Vendor", font='Futura Std Medium', font_size=50,
                         color="#fff0d5").shift(3 * UP)
        for tick in per_graph.get_x_axis():
            tick.set_color("#fff0d5")
        for tick in per_graph.get_y_axis():
            tick.set_color("#fff0d5")
        self.play(ReplacementTransform(bar_graph, per_graph), ReplacementTransform(axis_labels, per_axis_labels),
                  ReplacementTransform(hist_title, per_title), Wait(3))
        self.play(Unwrite(per_graph), Unwrite(per_axis_labels), Unwrite(per_title), Wait(3))
        # Data Cleaning
        data_clean_title = Text("Data Cleaning", font='Futura Std Medium', font_size=70, color="#ff9955")\
            .shift(3.5*LEFT+3*UP)
        misspell_text = Paragraph("User data has many misspellings,", "unrealistic values, etc.",
                                  font='Futura Std Medium', font_size=50, color="#fff0d5", line_spacing=0.5)\
            .shift(1.5*UP)
        misspell_correct = Paragraph("Match vendor names and addresses", "by their levenshtein distance",
                                     font='Futura Std Medium', font_size=50, color="#55ffb5", line_spacing=0.5)\
            .move_to(misspell_text)
        missing_text = Paragraph("However, only one missing value!", font='Futura Std Medium', font_size=50,
                                 color="#fff0d5", line_spacing=0.5).next_to(misspell_text, DOWN, buff=0.5)
        missing_correct = Paragraph("Impute value with mean", "amount for corresponding company",
                                    font='Futura Std Medium', font_size=50, color="#55ffb5", line_spacing=0.5)\
            .move_to(missing_text)
        ocr_text = Paragraph("Needed to account for the variable", "position of important text in OCR", "data.",
                             font='Futura Std Medium', font_size=50, color="#fff0d5", line_spacing=0.5)\
            .next_to(missing_text, DOWN, buff=0.5)
        ocr_correct = Paragraph("Analyse multiple positions' levenshtein", "distance with known data",
                                font='Futura Std Medium', font_size=50, color="#55ffb5", line_spacing=1)\
            .move_to(ocr_text)
        self.play(DrawBorderThenFill(data_clean_title), FadeIn(misspell_text, shift=UP), Wait(2))
        self.play(FadeIn(missing_text, shift=UP), Wait(2))
        self.play(FadeIn(ocr_text, shift=UP), Wait(2))
        self.play(ReplacementTransform(misspell_text, misspell_correct), Wait(2))
        self.play(ReplacementTransform(missing_text, missing_correct), Wait(2))
        self.play(ReplacementTransform(ocr_text, ocr_correct), Wait(2))
        self.play(FadeOut(ocr_correct, missing_correct, misspell_correct, data_clean_title, scale=0.5))
        self.wait(2)


class DT23Part2(Scene):
    def construct(self):
        self.camera.background_color = "#001014"
        x_ran_min = ValueTracker(-10)
        x_ran_max = ValueTracker(10)
        x_ran_step = ValueTracker(1.5)
        y_ran_min = ValueTracker(-10)
        y_ran_max = ValueTracker(10)
        y_ran_step = ValueTracker(1.5)
        num_plane = always_redraw(lambda: NumberPlane(x_range=[x_ran_min.get_value(), x_ran_max.get_value(),
                                                               x_ran_step.get_value()],
                                                      y_range=[y_ran_min.get_value(), y_ran_max.get_value(),
                                                               y_ran_step.get_value()],
                                                      background_line_style={
                                                          "stroke_color": "#fff0d5",
                                                          "stroke_width": 3,
                                                          "stroke_opacity": 0.4
                                                      }))
        self.add(num_plane)
        # Matching Image Data
        receipt_image = ImageMobject("C:/Users/jackt/Documents/Datathon2023/00d0116788763.jpg").scale(0.55)
        frag1 = ImageMobject("C:/Users/jackt/Documents/Datathon2023/Frag1.png").scale(0.1)
        frag2 = ImageMobject("C:/Users/jackt/Documents/Datathon2023/Frag2.png").scale(0.1)
        frag3 = ImageMobject("C:/Users/jackt/Documents/Datathon2023/Frag3.png").scale(0.1)
        frag4 = ImageMobject("C:/Users/jackt/Documents/Datathon2023/Frag4.png").scale(0.1)
        frag5 = ImageMobject("C:/Users/jackt/Documents/Datathon2023/Frag5.png").scale(0.1)
        frag_group = Group(frag1, frag2, frag3, frag4, frag5)
        self.play(FadeIn(receipt_image, scale=0.5), FadeIn(frag_group), Wait(1.5))
        self.play(frag1.animate.scale(10).shift(2*UP+3*LEFT))
        self.play(frag2.animate.scale(10).shift(1.5 * UP + 3.5 * RIGHT))
        self.play(frag3.animate.scale(10).shift(UP + 3.5 * LEFT))
        self.play(frag4.animate.scale(10).shift(1.5 * DOWN + 2.5 * RIGHT))
        self.play(frag5.animate.scale(10).shift(0.5*DOWN+2.25 * LEFT))
        frag1_bb = SurroundingRectangle(frag1, color="#ff9955", stroke_width=5, fill_color=WHITE, fill_opacity=0.1,
                                        buff=0.02)
        frag1_c = Line(start=frag1_bb.get_bottom(), end=0.6 * UP + 0.4 * LEFT, color="#ff9955")
        frag2_bb = SurroundingRectangle(frag2, color="#ff9955", stroke_width=5, fill_color=WHITE, fill_opacity=0.1,
                                        buff=0.02)
        frag2_c = Line(start=frag2_bb.get_left(), end=1.55 * UP + 0.2 * RIGHT, color="#ff9955")
        frag3_bb = SurroundingRectangle(frag3, color="#ff9955", stroke_width=5, fill_color=WHITE, fill_opacity=0.1,
                                        buff=0.02)
        frag3_c = Line(start=frag3_bb.get_right(), end=0.95 * UP + 0.8 * LEFT, color="#ff9955")
        frag4_bb = SurroundingRectangle(frag4, color="#ff9955", stroke_width=5, fill_color=WHITE, fill_opacity=0.1,
                                        buff=0.02)
        frag4_c = Line(start=frag4_bb.get_top(), end=0.75 * DOWN + 1.1 * RIGHT, color="#ff9955")
        frag5_bb = SurroundingRectangle(frag5, color="#ff9955", stroke_width=5, fill_color=WHITE, fill_opacity=0.1,
                                        buff=0.02)
        frag5_c = Line(start=frag5_bb.get_right(), end=0.15 * DOWN + 1.3 * LEFT, color="#ff9955")
        fragbbc_group = VGroup(frag1_bb, frag1_c, frag2_bb, frag2_c, frag3_bb, frag3_c, frag4_bb, frag4_c, frag5_bb,
                               frag5_c)
        image_group = Group(receipt_image, frag_group, fragbbc_group)
        self.play(Write(fragbbc_group), Wait(3))
        self.play(image_group.animate.shift(2*LEFT).scale(0.8), Wait(2))
        ocr_image = ImageMobject("C:/Users/jackt/Documents/Datathon2023/OCR Screenshot.png").scale(0.2)\
            .shift(0.2*DOWN+3.5*RIGHT)
        ocr_convert_arrow = Arrow(start=image_group.get_center(), end=ocr_image.get_left(), color="#ff9955",
                                  stroke_width=5)
        ocr_text = Paragraph("Optical Character", "Recognition", font='Futura Std Medium', font_size=40,
                             color="#fff0d5").next_to(ocr_image, DOWN)
        self.play(DrawBorderThenFill(ocr_convert_arrow), Wait(2))
        self.play(FadeIn(ocr_image, shift=RIGHT), DrawBorderThenFill(ocr_text), Wait(3))
        self.play(FadeOut(image_group, ocr_image, scale=0.5), Unwrite(ocr_convert_arrow), Uncreate(ocr_text), Wait(2))
        # Matching OCR Data
        ocr1 = ImageMobject("C:/Users/jackt/Documents/Datathon2023/Paper Icon.png").scale(0.15)
        ocr2 = ocr1.copy()
        ocr3 = ocr1.copy()
        ocr4 = ocr1.copy()
        ocr_doc_group = Group(ocr1, ocr2, ocr3, ocr4).arrange(buff=0.5).shift(3.5*LEFT)
        ocr_title = Text("OCRs", font='Futura Std Medium', font_size=50, color="#fff0d5").next_to(ocr_doc_group, UP)
        money_text = Text("Money", font='Futura Std Medium', font_size=30, color="#fff0d5")
        date_text = Text("Date", font='Futura Std Medium', font_size=30, color="#fff0d5")
        name_text = Text("Name", font='Futura Std Medium', font_size=30, color="#fff0d5")
        address_text = Text("Address", font='Futura Std Medium', font_size=30, color="#fff0d5")
        pot_matrix = Matrix([["[PotC_1,\\cdots]", "\\cdots"],
                             ["[PotC_2,\\cdots]", "\\cdots"],
                             ["\\vdots", "\\ddots"],
                             ["[PotC_n,\\cdots]", "\\cdots"]]).set_color("#fff0d5").shift(3.5*RIGHT)
        pot_text = Text("Candidates", font='Futura Std Medium', font_size=50, color="#fff0d5")\
            .next_to(pot_matrix, UP)
        ocr_attr_arrow = Arrow(start=ocr_doc_group.get_right(), end=pot_matrix.get_left(), color="#ff9955",
                               stroke_width=10)
        attribute_group = VGroup(money_text, date_text, name_text, address_text).arrange(DOWN, buff=0.5).move_to(
            ocr_attr_arrow)
        plus_text = Text("+", font='Futura Std Medium', font_size=40, color="#fff0d5") \
            .next_to(address_text, DOWN)
        leven_thresh = Text("Levenshtein Threshold", font='Futura Std Medium', font_size=40, color="#fff0d5") \
            .next_to(plus_text, DOWN)
        weight_text = Text("Find best attribute weights with gradient descent", font='Futura Std Medium', font_size=45,
                           color="#001014")
        weight_border = SurroundingRectangle(weight_text, color="#fff0d5", fill_color="#fff0d5", fill_opacity=0.8,
                                             buff=0.3)
        self.play(FadeIn(ocr_doc_group, scale=0.5), Write(ocr_title, run_time=1), Wait(2))
        self.play(Write(ocr_attr_arrow), Write(attribute_group), Wait(2.5))
        self.play(Write(plus_text), Write(leven_thresh), Wait(2.5))
        self.play(DrawBorderThenFill(pot_matrix), Write(pot_text), Wait(2.5))
        self.play(Create(weight_border))
        self.play(DrawBorderThenFill(weight_text), Wait(2))
        self.play(FadeOut(weight_border, weight_text, leven_thresh, plus_text, attribute_group, ocr_doc_group,
                          ocr_attr_arrow, pot_matrix, ocr_title, pot_text, shift=DOWN), Wait(2))
        # Gradient Descent
        axes2 = always_redraw(lambda: Axes(x_range=[x_ran_min.get_value(), x_ran_max.get_value(),
                                                    x_ran_step.get_value()],
                                           y_range=[x_ran_min.get_value(), x_ran_max.get_value(),
                                                    x_ran_step.get_value()], x_length=20*x_ran_step.get_value()/1.5,
                                           y_length=20*y_ran_step.get_value()/1.5,
                              axis_config={"include_tip": True, "numbers_to_exclude": [0]}
                                           ).add_coordinates().set_color("#fff0d5"))
        receipt_dot = Dot(ORIGIN, color="#ff5555")
        receipt_label = Text("R", font='Futura Std Medium', font_size=30, color="#fff0d5")\
            .next_to(receipt_dot, DOWN+RIGHT, buff=0.1)
        cand_dot1 = always_redraw(lambda: Dot(axes2.coords_to_point(1.6, 1.7), color="#ff9955"))
        cand_dot2 = always_redraw(lambda: Dot(axes2.coords_to_point(0.7, 1), color="#ff9955"))
        cand_dot3 = always_redraw(lambda: Dot(axes2.coords_to_point(1, 2), color="#ff9955"))
        cand_dot4 = always_redraw(lambda: Dot(axes2.coords_to_point(1.5, 0.4), color="#ff9955"))
        cand_label1 = always_redraw(lambda: Text("1", font='Futura Std Medium', font_size=30, color="#fff0d5") \
            .next_to(cand_dot1, UP + RIGHT, buff=0.1))
        cand_label2 = always_redraw(lambda: Text("2", font='Futura Std Medium', font_size=30, color="#fff0d5") \
            .next_to(cand_dot2, UP + RIGHT, buff=0.1))
        cand_label3 = always_redraw(lambda: Text("3", font='Futura Std Medium', font_size=30, color="#fff0d5") \
            .next_to(cand_dot3, UP + RIGHT, buff=0.1))
        cand_label4 = always_redraw(lambda: Text("4", font='Futura Std Medium', font_size=30, color="#fff0d5") \
            .next_to(cand_dot4, UP + RIGHT, buff=0.1))
        cand_line1 = always_redraw(lambda: DashedLine(start=cand_dot1.get_center(), end=ORIGIN, color="#fff0d5",
                                                      stroke_width=5))
        cand_line2 = always_redraw(lambda: DashedLine(start=cand_dot2.get_center(), end=ORIGIN, color="#fff0d5",
                                                      stroke_width=5))
        cand_line3 = always_redraw(lambda: DashedLine(start=cand_dot3.get_center(), end=ORIGIN, color="#fff0d5",
                                                      stroke_width=5))
        cand_line4 = always_redraw(lambda: DashedLine(start=cand_dot4.get_center(), end=ORIGIN, color="#fff0d5",
                                                      stroke_width=5))
        cand_bor2 = always_redraw(lambda: SurroundingRectangle(cand_dot2, color="#ff5555", stroke_width=5, buff=0.2))
        cand_dot_group = VGroup(cand_line1, cand_line2, cand_line3, cand_line4, cand_dot1, cand_dot2, cand_dot3,
                                cand_dot4, cand_label1, cand_label2, cand_label3, cand_label4, cand_bor2)
        dist_expre = MathTex("\\sqrt{(w_xd_x)^2+(w_yd_y)^2}", font_size=60, color="#fff0d5").shift(3*UP+3.9*LEFT)
        weight_x = 1
        weight_x_text = MathTex("w_x", font_size=60)
        weight_x_var = Variable(weight_x, weight_x_text, num_decimal_places=2).set_color("#fff0d5")\
            .next_to(dist_expre, DOWN).shift(1.5*LEFT)
        weight_y = 1
        weight_y_text = MathTex("w_y", font_size=60)
        weight_y_var = Variable(weight_y, weight_y_text, num_decimal_places=2).set_color("#fff0d5") \
            .next_to(dist_expre, DOWN).shift(1.5*RIGHT)
        expre_group = VGroup(dist_expre, weight_y_var, weight_x_var)
        expre_border = SurroundingRectangle(expre_group, color="#ff9955", stroke_width=7, fill_color=WHITE,
                                            fill_opacity=0.1, buff=0.2)
        self.play(DrawBorderThenFill(axes2), Wait(2))
        self.play(DrawBorderThenFill(receipt_dot), DrawBorderThenFill(receipt_label), Wait(2))
        self.play(Write(cand_dot_group[4:-1]), Wait(3))
        self.play(Write(expre_group), Create(expre_border), Wait(2.5))
        self.play(Create(cand_dot_group[0:4]), Wait(2))
        self.play(Create(cand_bor2), Wait(2))
        self.play(weight_y_var.tracker.animate.set_value(3).set_color("#ff5555"), y_ran_step.animate.set_value(3),
                  Wait(2))
        cand_bor4 = always_redraw(lambda: SurroundingRectangle(cand_dot4, color="#ff5555", stroke_width=5, buff=0.2))
        self.play(Uncreate(cand_bor2), Create(cand_bor4), Wait(2))
        self.play(FadeOut(axes2, cand_dot_group, cand_bor4, expre_group, expre_border), Wait(2))
        # Conclusion
        conclusion_title = Text("Conclusion", font='Futura Std Medium', font_size=70, color="#ff9955").shift(3*UP)
        model_accuracy = Paragraph("The final model was able to", "achieve an accuracy of 82%.",
                                   font='Futura Std Medium', font_size=50, color="#001014", line_spacing=1,
                                   t2c={"82%": "#ff5555"})
        model_importance = Paragraph("Vendor address and name were", "particularly valuable for correctly",
                                     "matching receipts", font='Futura Std Medium', font_size=50, color="#001014",
                                     line_spacing=1)
        challenge_text = Paragraph("While challenging to work with", "our model was able to handily ",
                                   "overcome these obstacles", font='Futura Std Medium', font_size=50, color="#001014",
                                   line_spacing=1)
        thanks_text = Text("Thanks for Watching!", font='Futura Std Medium', font_size=50, color="#ff5555")
        text_background = SurroundingRectangle(model_importance, color="#fff0d5", fill_color="#fff0d5",
                                               fill_opacity=0.5)
        self.play(DrawBorderThenFill(text_background), DrawBorderThenFill(conclusion_title), Write(model_accuracy),
                  Wait(3))
        self.play(TransformMatchingShapes(model_accuracy, model_importance), Wait(2))
        self.play(TransformMatchingShapes(model_importance, challenge_text), Wait(2))
        self.play(TransformMatchingShapes(challenge_text, thanks_text), Wait(2))


class DT23Part3D(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#001014"
        axes3 = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text("Concept easily generalizes!", font='Futura Std Medium', font_size=50, color="#fff0d5")
        text3d.to_corner(UL)
        receipt_sphere = Surface(
            lambda u, v: np.array([
                0.125 * np.cos(u) * np.cos(v),
                0.125 * np.cos(u) * np.sin(v),
                0.125 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2], checkerboard_colors=["#ff5555", "#ff5555"],
            resolution=(15, 32), stroke_color="#fff0d5", stroke_width=0.1
        )
        cand_sphere1 = Surface(
            lambda u, v: np.array([
                0.125 * np.cos(u) * np.cos(v),
                0.125 * np.cos(u) * np.sin(v),
                0.125 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2], checkerboard_colors=["#fff0d5", "#fff0d5"],
            resolution=(15, 32), stroke_color="#fff0d5", stroke_width=0.1
        ).move_to([1.6, 1.7, 2])
        cand_sphere2 = cand_sphere1.copy().move_to([0.7, 1, 0.2])
        cand_sphere3 = cand_sphere1.copy().move_to([1, 2, 1])
        cand_sphere4 = cand_sphere1.copy().move_to([1.5, 0.4, 0.5])
        cand_label1 = Text("1", font='Futura Std Medium', font_size=30, color="#fff0d5") \
                                    .next_to(cand_sphere1, UP + RIGHT, buff=0.1)
        cand_label2 = Text("2", font='Futura Std Medium', font_size=30, color="#fff0d5") \
                                    .next_to(cand_sphere2, UP + RIGHT, buff=0.1)
        cand_label3 = Text("3", font='Futura Std Medium', font_size=30, color="#fff0d5") \
                                    .next_to(cand_sphere3, UP + RIGHT, buff=0.1)
        cand_label4 = Text("4", font='Futura Std Medium', font_size=30, color="#fff0d5") \
                                    .next_to(cand_sphere4, UP + RIGHT, buff=0.1)
        cand_line1 = Line3D(start=cand_sphere1.get_center(), end=ORIGIN, color="#fff0d5")
        cand_line2 = Line3D(start=cand_sphere2.get_center(), end=ORIGIN, color="#fff0d5")
        cand_line3 = Line3D(start=cand_sphere3.get_center(), end=ORIGIN, color="#fff0d5")
        cand_line4 = Line3D(start=cand_sphere4.get_center(), end=ORIGIN, color="#fff0d5")
        cand_group = VGroup(cand_sphere1, cand_sphere2, cand_sphere3, cand_sphere4, cand_line1, cand_line2, cand_line3,
                            cand_line4)
        cand_label_group = VGroup(cand_label1, cand_label2, cand_label3, cand_label4)
        dist_expre = MathTex("\\sqrt{(w_xd_x)^2+(w_yd_y)^2+(w_zd_z)^2}", font_size=60, color="#fff0d5")\
            .shift(3 * DOWN)
        self.add(axes3, receipt_sphere)
        self.add_fixed_in_frame_mobjects(text3d, dist_expre)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(Create(cand_group[0:4]), Write(cand_label_group), Wait(2))
        self.play(Create(cand_group[4:]), Wait(2))
        self.wait(5)
        self.stop_ambient_camera_rotation()


class DT23Fix4(Scene):
    def construct(self):
        self.camera.background_color = "#001014"
        # Summary of Results
        line_spacer2 = Paragraph("1.", "2.", "3.", font='Futura Std Medium', font_size=50, color="#ff9955",
                                 line_spacing=2).shift(6 * LEFT+0.2*DOWN)
        summary_text = Paragraph("To accomplish this, we created a pipeline", "consisting of:",
                                 font='Futura Std Medium', font_size=50, color="#fff0d5").shift(3*UP)
        text_similar = Text("Text Similarity Analysis", font='Futura Std Medium', font_size=50, color="#fff0d5")\
            .next_to(line_spacer2[0], buff=0.5)
        image_recog = Text("Image Recognition", font='Futura Std Medium', font_size=50, color="#fff0d5")\
            .next_to(line_spacer2[1], buff=0.5)
        knn_algo = Text("Gradient Descent Algorithm", font='Futura Std Medium', font_size=50, color="#fff0d5")\
            .next_to(line_spacer2[2], buff=0.5)
        accuracy_text = Text("To match receipts with over 84% accuracy!", font='Futura Std Medium', font_size=50,
                             color="#fff0d5").shift(3.2*DOWN)
        diagram_text = Text("Place_Name1", font="Times New Roman", font_size=40, color="#fff0d5").shift(4*RIGHT+0*DOWN)
        diagram_text2 = Text("Plake_Bane1", font="Times New Roman", font_size=40, color="#fff0d5").shift(4*RIGHT+1*DOWN)
        diagram_arrow = CurvedArrow(start_point=diagram_text.get_right()+0.25*RIGHT,
                                    end_point=diagram_text2.get_right()+0.25*RIGHT,
                                    color="#ff9955", angle=-0.4 * PI)
        diagram_arrow2 = CurvedArrow(start_point=diagram_text2.get_left() + 0.25 * LEFT,
                                     end_point=diagram_text.get_left() + 0.25 * LEFT,
                                     color="#ff9955", angle=-0.4 * PI)
        diagram_border = SurroundingRectangle(VGroup(diagram_arrow, diagram_arrow2, diagram_text, diagram_text2),
                                              color="#ff9955", stroke_width=7, buff=0.2, fill_color=WHITE,
                                              fill_opacity=0.1)
        num_plane = NumberPlane(x_range=[-10, 10, 1.5], y_range=[-10, 10, 1.5],
                                background_line_style={
                                    "stroke_color": "#fff0d5",
                                    "stroke_width": 3,
                                    "stroke_opacity": 0.4
                                })
        self.add(num_plane)
        self.play(Write(summary_text, run_time=1.5), DrawBorderThenFill(line_spacer2), Wait(2))
        self.play(FadeIn(text_similar, shift=UP), DrawBorderThenFill(diagram_text, run_time=1), Write(diagram_text2),
                  Create(diagram_arrow), Create(diagram_border), Create(diagram_arrow2), Wait(2))
        self.play(FadeIn(image_recog, shift=UP), Wait(1.5))
        self.play(FadeIn(knn_algo, shift=UP), Wait(1.5))
        self.play(FadeIn(accuracy_text, shift=UP), Wait(1.5))
        self.play(FadeOut(summary_text, line_spacer2, text_similar, diagram_text, diagram_text2, diagram_arrow,
                          diagram_arrow2, diagram_border, image_recog, knn_algo, accuracy_text, shift=DOWN), Wait(2))


class DT23Fix5(Scene):
    def construct(self):
        self.camera.background_color = "#001014"
        # Conclusion
        conclusion_title = Text("Conclusion", font='Futura Std Medium', font_size=70, color="#ff9955").shift(3 * UP)
        model_accuracy = Paragraph("The final model was able to", "achieve an accuracy of 84.2%.",
                                   font='Futura Std Medium', font_size=50, color="#001014", line_spacing=1,
                                   t2c={"84.2%": "#ff5555"})
        model_importance = Paragraph("Date was particularly valuable for",
                                     "correctly matching receipts", font='Futura Std Medium', font_size=50,
                                     color="#001014", line_spacing=1)
        thanks_text = Text("Thanks for Watching!", font='Futura Std Medium', font_size=50, color="#ff5555")
        text_background = SurroundingRectangle(model_importance, color="#fff0d5", fill_color="#fff0d5",
                                               fill_opacity=0.5)
        self.play(DrawBorderThenFill(text_background), DrawBorderThenFill(conclusion_title), Write(model_accuracy),
                  Wait(3))
        self.play(TransformMatchingShapes(model_accuracy, model_importance), Wait(2))
        self.play(TransformMatchingShapes(model_importance, thanks_text), Wait(2))