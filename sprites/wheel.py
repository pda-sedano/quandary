import math
import numpy as np
import pygame as pg


# parameters
radius = 300
circle_color = (100, 100, 100)
line_color = (255, 0, 0)
line_width = 3

guide_radius = 400
minor_guide_line_length = 50
major_guide_line_length = 80
guide_line_color = (0, 0, 255)
guide_line_width = 3
minor_guide_angle_increment = math.tau / 16
major_guide_angle_increment = math.tau / 8
snap_tolerance = 0.03

clear = (0, 0, 0, 0)


class Wheel(pg.sprite.Sprite):
    """A rotatable circle that allows selection of an angle."""
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((2 * guide_radius, 2 * guide_radius))
        self.rect = self.image.get_rect()
        self.dragging = False
        self.angle = 0
        self.offset_angle = 0
        self.draw()

    def draw(self):
        # Draw scroll circle
        pg.draw.circle(self.image, circle_color, (guide_radius, guide_radius), radius)
        pg.draw.line(self.image, line_color, (guide_radius, guide_radius),
                     (guide_radius + radius * np.cos(self.angle), guide_radius + radius * np.sin(self.angle)),
                     line_width)

        # Draw guide lines
        for theta in np.arange(0, math.tau, minor_guide_angle_increment):
            guide_line_length = major_guide_line_length if (theta % major_guide_angle_increment == 0) \
                else minor_guide_line_length
            pg.draw.line(self.image, guide_line_color,
                         (guide_radius + (guide_radius - guide_line_length) * np.cos(theta),
                          guide_radius + (guide_radius - guide_line_length) * np.sin(theta)),
                         (guide_radius * (1 + np.cos(theta)), guide_radius * (1 + np.sin(theta))), guide_line_width)

    def update(self, event=None):
        if event is not None:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.dragging = self.rect.collidepoint(event.pos)
                self.offset_angle = np.arctan2(event.pos[1] - self.rect.centery,
                                        event.pos[0] - self.rect.centerx) - self.angle
            elif event.type == pg.MOUSEBUTTONUP:
                self.dragging = False

        # check if we're still within the circle
        if (pg.mouse.get_pos()[0] - self.rect.centerx) ** 2 + (pg.mouse.get_pos()[1] - self.rect.centery) ** 2 \
                > radius ** 2:
            self.dragging = False

        if self.dragging:
            self.angle = np.arctan2(pg.mouse.get_pos()[1] - self.rect.centery,
                                    pg.mouse.get_pos()[0] - self.rect.centerx) - self.offset_angle

            # implement snapping
            # TODO: no reason to recalculate this every time
            for theta in np.arange(0, math.tau, minor_guide_angle_increment):
                if np.abs(self.angle % math.tau - theta) < snap_tolerance:
                    self.angle = theta

            self.image.fill(clear)
            self.draw()
