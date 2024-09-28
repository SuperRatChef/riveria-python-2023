# tee ratkaisu tänne
def ilman_vokaaleja(mjono: str):
    vokaalit = "aeiouyäöå"
    mjono_konsonantit = ""
    for kirjain in mjono:
        if(vokaalit.count(kirjain) == 0):
            mjono_konsonantit += kirjain
    return mjono_konsonantit