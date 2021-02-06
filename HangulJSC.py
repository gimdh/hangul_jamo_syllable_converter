
class HangulJSC:
    def contains_jamo(self, str):
        return any(char for char in str if 0x1100 <= char and char <= 0x11FF)

    # 0x115F, 0x1160 are empty charcters whose usage is unclear AFAIK
    # So they are considered nonconvertible now

    def contains_nonconvertible_jamo(self, str):
        return any(char for char in str if (0x1113 <= char and char <= 0x1160) or
                                            (0x1176 <= char and char <= 0x11A7) or
                                            (0x11C3 <= char and char <= 0x11FF))

    def contains_convertible_jamo(self, str):
        return any(char for char in str if (0x1100 <= char and char <= 0x1112) or
                                            (0x1161 <= char and char <= 0x1175) or
                                            (0x11A8 <= char and char <= 0x11C2))

    def jamo_to_syllable(self, str):
        success = False

        

        return success

    def syllable_to_jamo(self, str):
        success = False

        return success