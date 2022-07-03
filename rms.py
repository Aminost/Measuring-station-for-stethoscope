# Code Writing by Mohamed Amine Guedria
# Guedria.amine@gmail.com
# This code calculate the Effective Voltage(Vrms)

import struct
import math

SHORT_NORMALIZE = (0.1/(32768))

class voltage(object):
    def get_rms(data):#calculate the Effective Voltage(Vrms)
        count = len(data) / 2
        format = "%dh" % (count)
        shorts = struct.unpack(format, data)

        # iterate over the block.
        sum_squares = 0.0
        for sample in shorts:
            # sample is a signed short in +/- 32768.
            # normalize it to 1.0
            n = sample * SHORT_NORMALIZE
            sum_squares += n * n

        return math.sqrt(sum_squares / count)