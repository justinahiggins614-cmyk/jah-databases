#!/usr/bin/env python3
"""PHASE J demo archetypes: institution profile (colleges) and stats (schools).

Each generated program embeds the record's own public data (founded/
established year, campus or school counts, enrollment) and computes simple,
real summaries from it. Every program prints an OK: marker and exits 0.
"""


def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (name, rid, group))


def demo_profile(name, rid, group, founded_year, n_campuses, enrollment_num):
    """Institution profile analyzer: age, campuses, enrollment density."""
    code = _hdr(name, rid, group)
    code += (
        "FOUNDED = %d\n"
        "CAMPUSES = %d\n"
        "ENROLLMENT = %d\n"
        "CURRENT_YEAR = 2026\n\n"
        "def institution_age(founded, current_year=CURRENT_YEAR):\n"
        "    return current_year - founded\n\n"
        "def students_per_campus(enrollment, campuses):\n"
        "    return enrollment / campuses if campuses else 0\n\n"
        "def main():\n"
        "    age = institution_age(FOUNDED)\n"
        "    spc = students_per_campus(ENROLLMENT, CAMPUSES)\n"
        "    print(%r)\n"
        "    print('Founded %%d; %%d campus(es); about %%d students'\n"
        "          %% (FOUNDED, CAMPUSES, ENROLLMENT))\n"
        "    print('Age: %%d years; students per campus: %%.0f' %% (age, spc))\n"
        "    assert age > 0, 'founded year must be in the past'\n"
        "    assert spc > 0, 'enrollment must be positive'\n"
        "    print('OK: profile demo ran for %%s' %% %r)\n\n"
        "if __name__ == '__main__':\n"
        "    main()\n"
        % (founded_year, n_campuses, enrollment_num, name, rid))
    return code


def demo_stats(name, rid, group, established_year, enrollment_num, schools_num):
    """Public-school stats analyzer: years active, students per school."""
    code = _hdr(name, rid, group)
    code += (
        "ESTABLISHED = %d\n"
        "ENROLLMENT = %s\n"
        "SCHOOLS = %s\n"
        "CURRENT_YEAR = 2026\n\n"
        "def years_active(established, current_year=CURRENT_YEAR):\n"
        "    return current_year - established\n\n"
        "def students_per_school(enrollment, schools):\n"
        "    if enrollment is None or not schools:\n"
        "        return None\n"
        "    return enrollment / schools\n\n"
        "def main():\n"
        "    yrs = years_active(ESTABLISHED)\n"
        "    sps = students_per_school(ENROLLMENT, SCHOOLS)\n"
        "    print(%r)\n"
        "    print('Established %%d; active %%d years' %% (ESTABLISHED, yrs))\n"
        "    if ENROLLMENT is not None:\n"
        "        print('Enrollment about %%d' %% ENROLLMENT)\n"
        "    if sps is not None:\n"
        "        print('Students per school: %%.0f' %% sps)\n"
        "    assert yrs > 0, 'established year must be in the past'\n"
        "    print('OK: stats demo ran for %%s' %% %r)\n\n"
        "if __name__ == '__main__':\n"
        "    main()\n"
        % (established_year,
           "None" if enrollment_num is None else str(enrollment_num),
           "None" if schools_num is None else str(schools_num),
           name, rid))
    return code


DEMOS = {"profile": demo_profile, "stats": demo_stats}
