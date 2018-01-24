
# EQ-5D regression coefficients
Constant = 0.081
N3 = 0.269
#dictionary
dictCoefficients = {'Mobility':             [0, 0.069, 0.314],
                    'Self-Care':            [0, 0.104, 0.214],
                    'Usual Activity':       [0, 0.036, 0.094],
                    'Pain/Discomfort':      [0, 0.123, 0.386],
                    'Anxiety/Depression':   [0, 0.071, 0.236]};

#two quote and click return to get the param

def get_score(mobility,self_care, usual_activity,pain_discomfort,anxiety_depression):
        """

        :param mobility: level of mobility dimension
        :param self_care:
        :param usual_activity:
        :param pain_discomfort:
        :param anxiety_depression:
        :return: EQ-5D preference score
        """

        #check the level
        if not(mobility in [1,2,3]):
            raise ValueError("Mobility level can take only 1,2 or 3")
        if not (self_care in [1, 2, 3]):
            raise ValueError('Self-care level can take only 1, 2 or 3')
        if not (usual_activity in [1, 2, 3]):
            raise ValueError('Usual activity level can take only 1, 2 or 3')
        if not (pain_discomfort in [1, 2, 3]):
            raise ValueError('Pain/discomfort level can take only 1, 2 or 3')
        if not (anxiety_depression in [1, 2, 3]):
            raise ValueError('Anxiety level can take only 1, 2 or 3')


        score = 1
        if (mobility*self_care*usual_activity*pain_discomfort*anxiety_depression>1):
            score -= Constant

        if (max(mobility,self_care,usual_activity,pain_discomfort,anxiety_depression)==3):
            score -= N3

        score -= dictCoefficients['Mobility'][mobility-1]
        #python counts from 0
        score -= dictCoefficients['Self-Care'][self_care - 1]
        score -= dictCoefficients['Usual Activity'][usual_activity - 1]
        score -= dictCoefficients['Pain/Discomfort'][pain_discomfort - 1]
        score -= dictCoefficients['Anxiety/Depression'][anxiety_depression - 1]

        return score


