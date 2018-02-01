# -*- coding: utf-8 -*-

# யாப்பு
# தமிழ் பாக்களை ஆராய உதவுகிறது
#
# காப்புரிமை 2018, ஶ்ரீரமண ஶர்மா
# Copyright 2018, Shriramana Sharma
#
# பயனர் உரிமம்/User license: GNU Affero GPL v3+
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


__all__ = ["பாக்கள்", "நேர்", "நிரை", "தளைகள்"]


###
# ஒருங்குறி தமிழ் எழுத்துறுப்புகளின் வகைகள்

குறில்_உயிர் = "அஇஉஎஒ"
நெடில்_உயிர் = "ஆஈஊஏஓஐஔ"
உயிர் = குறில்_உயிர் + நெடில்_உயிர்
குறில்_உயிர்க்_குறி = "\u0BBF\u0BC1\u0BC6\u0BCA\u0BC8"  # \u0BC8 ை என்பது பொதுவாகக் குறிலாகவும் சீர் முதலில் மட்டுமே நெடிலாகவும் கொள்ளப்படுகிறது
நெடில்_உயிர்க்_குறி = "\u0BBE\u0BC0\u0BC2\u0BC7\u0BCB\u0BCC"
உயிர்க்_குறி = குறில்_உயிர்க்_குறி + நெடில்_உயிர்க்_குறி
அகரமேறிய_மெய் = "கஙசஞடணதநபமயரலவழளறனஜஶஷஸஹ"
புள்ளி = "்"
தமிழ்_எழுத்துறுப்புகள் = உயிர் + உயிர்க்_குறி + அகரமேறிய_மெய் + புள்ளி


###
# தமிழ் எழுத்துக்களின் எழுத்துறுப்பு இலக்கணம்

உயிருள்ள_எழுத்து = "(?:[" + அகரமேறிய_மெய் + "](?!" + புள்ளி + ")[" + உயிர்க்_குறி + "]?" + \
        "|[" + உயிர் + "])"
# ஒரு அகரமேறிய மெய், அதனுடன் ஒரு உயிர்க்குறி இருக்கலாம்
# அல்லது தனி உயிர்

குறில்_எழுத்து = "(?:[" + அகரமேறிய_மெய் + "][" + குறில்_உயிர்க்_குறி + "]?" + \
        "|[" + குறில்_உயிர் + "])"
# ஒரு அகரமேறிய மெய், அதனுடன் ஒரு குறில் உயிர்க் குறி இருக்கலாம்
# அல்லது தனி குறில் உயிர்

நெடில்_எழுத்து = "(?:[" + அகரமேறிய_மெய் + "][" + நெடில்_உயிர்க்_குறி + "]" + \
        "|[" + நெடில்_உயிர் + "])"
# ஒரு நெடிலேறிய மெய், அல்லது தனி நெடில் உயிர்  # இது தற்சமயம் பயன்பாட்டில் இல்லை

ஐகார_எழுத்து = "(?:[" + அகரமேறிய_மெய் + "]ை" \
        "|ஐ)"
# ஒரு ஐகாரமேறிய மெய், அல்லது தனி ஐகாரம்

மெய்_எழுத்து = "(?:[" + அகரமேறிய_மெய் + "]்)"


###
# அடி, சீர், அசை – இவற்றின் இலக்கணங்கள்

அடி_இலக்கணம் = "[^\n]*\n"
சீர்_இலக்கணம் = "[" + தமிழ்_எழுத்துறுப்புகள் + "]+"

சீர்_முதல்_ஐகார_நேர்_அசை_இலக்கணம் = "(?<![" + தமிழ்_எழுத்துறுப்புகள் + "])" + ஐகார_எழுத்து + மெய்_எழுத்து + "*"
நிரை_அசை_இலக்கணம் = குறில்_எழுத்து + உயிருள்ள_எழுத்து + மெய்_எழுத்து + "*"
பொதுவான_நேர்_அசை_இலக்கணம் = உயிருள்ள_எழுத்து + மெய்_எழுத்து + "*"


###
# compile செய்த வடிவங்கள்

import re
அடி_வடிவம் = re.compile(அடி_இலக்கணம்)
சீர்_வடிவம் = re.compile(சீர்_இலக்கணம்)
அசை_வடிவம் = re.compile("(" + சீர்_முதல்_ஐகார_நேர்_அசை_இலக்கணம் + ")|(" + நிரை_அசை_இலக்கணம் + ")|(" + பொதுவான_நேர்_அசை_இலக்கணம் + ")")
# முதலில் நிரையா என்று பார்த்த பிறகே நேரா என்று பார்க்கவேண்டும்
# ஏனெனில் ஓருயிர் மட்டுமான நேர் முதலில் கிடைத்துவிட்டால்
# அதன் பிறகு இரண்டுயிர் கொண்ட நிரை கிடைக்காது
#
# கவனிக்க:
# மொழி முதலை அலகிடுவது எளிதில்லை ஆகையாலும் வகையுளி என்பதாக மொழியிடையே சீரைப் பிரிப்பது
# தவிர்க்கப்படுவதாலும் சீர்முதலில் வரும் ஐகாரத்தை நெடிலாகக்கொண்டு மற்றவிடத்தில் வருவதைக் குறிலாகக் கொள்கிறோம்.
# ஐ என்ற தனி எழுத்துறுப்பு மொழி முதலில் தான் பயன்படும் ஆகையால் அதனை நெடிலாகத் தான் கொள்கிறோம்.


###
# அசைப் பெயர்கள், சீர் வாய்ப்பாடுகள், தளைப் பெயர்கள், அவற்றின் தெரிவு

நேர், நிரை, நாள், மலர், மா, விளம், காய், கனி, பூ, நிழல் = "நேர்", "நிரை", "நாள்", "மலர்", "மா", "விளம்", "காய்", "கனி", "பூ", "நிழல்"

இயற்சீர்_வெண்டளை, வெண்சீர்_வெண்டளை = "இயற்சீர் வெண்டளை", "வெண்சீர் வெண்டளை"
நேரொன்றிய_ஆசிரியத்தளை, நிரையொன்றிய_ஆசிரியத்தளை = "நேரொன்றிய ஆசிரியத்தளை", "நிரையொன்றிய ஆசிரியத்தளை"
கலித்தளை, ஒன்றிய_வஞ்சித்தளை, ஒன்றா_வஞ்சித்தளை = "கலித்தளை", "ஒன்றிய வஞ்சித்தளை", "ஒன்றா வஞ்சித்தளை"
தளைகள் = (இயற்சீர்_வெண்டளை, வெண்சீர்_வெண்டளை,
          நேரொன்றிய_ஆசிரியத்தளை, நிரையொன்றிய_ஆசிரியத்தளை,
          கலித்தளை, ஒன்றிய_வஞ்சித்தளை, ஒன்றா_வஞ்சித்தளை)

சீர்_வாய்ப்பாடுகள்_ஈற்றசைப்பெயர்கள்_தெரிவு = {
    (நேர்,): ("நாள்", நாள்),
    (நிரை,): ("மலர்", மலர்),
    (நேர், நேர்,): ("தே·மா", மா),
    (நிரை, நேர்,): ("புளி·மா", மா),
    (நேர், நிரை,): ("கூ·விளம்", விளம்),
    (நிரை, நிரை,): ("கரு·விளம்", விளம்),
    (நேர், நேர், நேர்,): ("தே·மாங்·காய்", காய்),
    (நிரை, நேர், நேர்,): ("புளி·மாங்·காய்", காய்),
    (நேர், நிரை, நேர்,): ("கூ·விளங்·காய்", காய்),
    (நிரை, நிரை, நேர்,): ("கரு·விளங்·காய்", காய்),
    (நேர், நேர், நிரை,): ("தே·மாங்·கனி", கனி),
    (நிரை, நேர், நிரை,): ("புளி·மாங்·கனி", கனி),
    (நேர், நிரை, நிரை,): ("கூ·விளங்·கனி", கனி),
    (நிரை, நிரை, நிரை,): ("கரு·விளங்·கனி", கனி),
    (நேர், நேர், நேர், நேர்,): ("தே·மாந்·தண்·பூ", பூ),
    (நேர், நேர், நிரை, நேர்,): ("தே·மா·நறும்·பூ", பூ),
    (நிரை, நேர், நேர், நேர்,): ("புளி·மாந்·தண்·பூ", பூ),
    (நிரை, நேர், நிரை, நேர்,): ("புளி·மா·நறும்·பூ", பூ),
    (நேர், நிரை, நேர், நேர்,): ("கூ·விளந்·தண்·பூ", பூ),
    (நேர், நிரை, நிரை, நேர்,): ("கூ·விள·நறும்·பூ", பூ),
    (நிரை, நிரை, நேர், நேர்,): ("கரு·விளந்·தண்·பூ", பூ),
    (நிரை, நிரை, நிரை, நேர்,): ("கரு·விள·நறும்·பூ", பூ),
    (நேர், நேர், நேர், நிரை,): ("தே·மாந்·தண்·ணிழல்", நிழல்),
    (நேர், நேர், நிரை, நிரை,): ("தே·மா·நறு·நிழல்", நிழல்),
    (நிரை, நேர், நேர், நிரை,): ("புளி·மாந்·தண்·ணிழல்", நிழல்),
    (நிரை, நேர், நிரை, நிரை,): ("புளி·மா·நறு·நிழல்", நிழல்),
    (நேர், நிரை, நேர், நிரை,): ("கூ·விளந்·தண்·ணிழல்", நிழல்),
    (நேர், நிரை, நிரை, நிரை,): ("கூ·விள·நறு·நிழல்", நிழல்),
    (நிரை, நிரை, நேர், நிரை,): ("கரு·விளந்·தண்·ணிழல்", நிழல்),
    (நிரை, நிரை, நிரை, நிரை,): ("கரு·விள·நறு·நிழல்", நிழல்),
}

தளை_தெரிவு = {
    (மா, நிரை): இயற்சீர்_வெண்டளை,
    (விளம், நேர்): இயற்சீர்_வெண்டளை,
    (காய், நேர்): வெண்சீர்_வெண்டளை,
    (மா, நேர்): நேரொன்றிய_ஆசிரியத்தளை,
    (விளம், நிரை): நிரையொன்றிய_ஆசிரியத்தளை,
    (காய், நிரை): கலித்தளை,
    (கனி, நிரை): ஒன்றிய_வஞ்சித்தளை,
    (கனி, நேர்): ஒன்றா_வஞ்சித்தளை
}


###
# செய்யுள் உறுப்பு வகைகள்


class அசை:
    """
    இதில் ஒரு அசையில் உள்ள எழுத்துக்கள் (மொழி) மற்றும் அசையின் பெயர் உள்ளடங்குகின்றன.
    """

    def __init__(தான், அசை_ஒப்பு):
        தான்.ஒப்பு = அசை_ஒப்பு
        தான்.பெயர் = நிரை if அசை_ஒப்பு.group(2) else நேர்

    def __getattr__(தான், உறுப்பு):  # தேவையெனில் மட்டும் உருவாக்கிக்கொள்ள
        if உறுப்பு == "மொழி":
            return தான்.ஒப்பு.group(0)
        elif உறுப்பு == "தொடக்கம்":
            return தான்.ஒப்பு.start()
        elif உறுப்பு == "முடிவு":
            return தான்.ஒப்பு.end()
        else:
            raise AttributeError("‘அசை’ பொருளுக்கு ‘{}’ என்ற உறுப்பு கிடையாது".format(உறுப்பு))

    def __repr__(தான்):
        return "‘{}’: {}".format(தான்.மொழி, தான்.பெயர்)


class சீர்(list):
    """
    சீரை அசைகளாகப் பிரித்துக்கொள்ளவும், சீரின் வாய்ப்பாடு, ஈற்றசையின் பெயர் (தளை மற்றும் ஓசைக்குத் தேவை) மற்றும்
    இந்த சீருக்கும் அதற்குப் பின் வரும் சீருக்கும் (அப்படி ஒன்று இருப்பின்) ஏற்படும் தளையை அறியவும் இது பயன்படுகிறது.
    """

    def __init__(தான், சீர்_ஒப்பு):

        super().__init__()
        தான்.ஒப்பு = சீர்_ஒப்பு
        தான்.அலகிடுக()  # பிறகு குற்றியலுகரம் நீக்க விரும்பலாம் என்பதால் தனியாக அமைத்தது

    def அலகிடுக(தான், குற்றியலுகரம்_நீக்கு = False):

        தான்.clear()
        # அடுத்த வரியில் குற்றியலுகரமும் அதற்கு முன் நிற்கும் (அகரமேறிய) மெய்யும் நீக்க -2
        for அசை_ஒப்பு in அசை_வடிவம்.finditer(தான்.ஒப்பு.string, தான்.ஒப்பு.start(), தான்.ஒப்பு.end() - (2 if குற்றியலுகரம்_நீக்கு else 0)):
            தான்.append(அசை(அசை_ஒப்பு))

        தான்.நீளத்தவறு = not (0 < len(தான்) < 5)  # ஏற்பு: குறைந்தது 1, மிகுதியாக 4
        if தான்.நீளத்தவறு:
            தான்.வாய்ப்பாடு, தான்.ஈற்றசைப்பெயர் = None, None
        else:
            தான்.வாய்ப்பாடு, தான்.ஈற்றசைப்பெயர் = சீர்_வாய்ப்பாடுகள்_ஈற்றசைப்பெயர்கள்_தெரிவு[tuple(அசை.பெயர் for அசை in தான்)]
        தான்.தளை = None  # அடுத்த சீரைக் கண்டபின் பதிவிடப்படும்

    def __getattr__(தான், உறுப்பு):  # தேவையெனில் மட்டும் உருவாக்கிக்கொள்ள
        if உறுப்பு == "மொழி":
            தான்.மொழி = "·".join(அசை.மொழி for அசை in தான்)
            return தான்.மொழி
        elif உறுப்பு == "அசைப்பெயர்கள்":
            தான்.அசைப்பெயர்கள் = "·".join(அசை.பெயர் for அசை in தான்)
            return தான்.அசைப்பெயர்கள்
        else:
            raise AttributeError("‘சீர்’ பொருளுக்கு ‘{}’ என்ற உறுப்பு கிடையாது".format(உறுப்பு))

    def __repr__(தான்):
        return "‘{}’, {}{}{}".format(தான்.மொழி, தான்.அசைப்பெயர்கள்,
                                     (", " + தான்.வாய்ப்பாடு) if தான்.வாய்ப்பாடு else "",
                                     (", " + தான்.தளை) if தான்.தளை else "")


class அடி(list):
    """
    அடியைச் சீர்களாகப் பிரித்துக்கொள்ளவும் அவைகளாலான நீளத்தால் ஏற்படும் பெயரை அறியவும் இது பயன்படுகிறது.
    """

    நீளப்பெயர்கள் = ((3, "குறளடி"), (4, "சிந்தடி"), (5, "அளவடி"), (6, "நெடிலடி"), (9, "கழி நெடிலடி"), (11, "இடையாகு கழி நெடிலடி"), (17, "கடையாகு கழி நெடிலடி"))

    def __init__(தான், உள்ளீட்டு_வரி, கடந்த_சீர்):

        super().__init__()
        தான்.உள்ளீட்டு_வரி = உள்ளீட்டு_வரி

        for சீர்_ஒப்பு in சீர்_வடிவம்.finditer(உள்ளீட்டு_வரி):
            இச்சீர் = சீர்(சீர்_ஒப்பு)
            if not len(இச்சீர்):  # வெறும் உயிர்க்குறிகள் தவறாக உள்ளிடப்பட்டிருந்தால் சீர் ஆகாது
                continue
            if கடந்த_சீர் and கடந்த_சீர்[-1].மொழி[-1] == "ு" and இச்சீர்[0].மொழி[0] in உயிர்:  # சீரிறுதி குற்றியலுகரம் முன் உயிர்
                கடந்த_சீர்.அலகிடுக(குற்றியலுகரம்_நீக்கு = True)
                # கவனிக்க: இப்படி அலகீட்டில் சரிசெய்தாலும் கடந்த_சீர் முந்தைய வரியில் இருந்தால் QSyntaxHighlighter சரியாகக் காட்டாமல் இருக்கலாம்
            தான்.append(இச்சீர்)
            if கடந்த_சீர் and len(கடந்த_சீர்) in (2, 3) and len(இச்சீர்):
                கடந்த_சீர்.தளை = தளை_தெரிவு[(கடந்த_சீர்.ஈற்றசைப்பெயர், இச்சீர்[0].பெயர்)]
            கடந்த_சீர் = இச்சீர்

        தான்.நீளத்தவறு = not (1 < len(தான்) < 17)  # ஏற்பு: குறைந்தது 2, மிகுதியாக 16
        சீர்_எண்ணிக்கை = len(தான்)
        for எல்லை, நீளப்பெயர் in அடி.நீளப்பெயர்கள்:
            if சீர்_எண்ணிக்கை < எல்லை:
                தான்.நீளப்பெயர் = நீளப்பெயர்
                break
        else:  # தவறான உள்ளீட்டால் 16க்கும் மேற்பட்ட சீர்கள் இருந்தால் பெயர் கிடையாது
            தான்.நீளப்பெயர் = None

    def __repr__(தான்):
        return தான்.நீளப்பெயர் + ":\n    " + "\n    ".join(str(சீர்) for சீர் in தான்)


class பா(list):
    """
    இதில் ஒரு பாவில் உள்ள அடிகள் உள்ளடங்குகின்றன. மேலும் பாவில் உள்ள தளைகளை எண்ணித் தருகிறது
    தற்சமயம் அதற்கு மேல் பாவின் வகை அறிவது போன்ற எதுவும் செய்ய முற்படவில்லை.
    """

    def __init__(தான், அடி_கொத்து):
        super().__init__(அடி_கொத்து)
        தான்.தளை_எண்ணிக்கை = {தளை: 0 for தளை in தளைகள்}
        தான்.மொத்த_தளைகள் = 0
        for அடி in அடி_கொத்து:
            for சீர் in அடி:
                if சீர்.தளை:
                    தான்.தளை_எண்ணிக்கை[சீர்.தளை] += 1
                    தான்.மொத்த_தளைகள் += 1

    def __repr__(தான்):
        return "\n".join("{} அடிப்பா".format(len(தான்)),
                         *(str(அடி) for அடி in தான்),
                         தான்.தளை_விவரம்())

    def தளை_விவரம்(தான்):
        if தான்.மொத்த_தளைகள் == 0:
            return ""
        இறங்குவரிசை = sorted(((தளை, தான்.தளை_எண்ணிக்கை[தளை] * 100 / தான்.மொத்த_தளைகள்) for தளை in தளைகள்), \
                             key = lambda அ: அ[1], reverse = True)  # குறையும் எண்ணிக்கையின் பேரில் தளைகளை வரிசையிடுக
        return ", ".join("{} {:.1f}%".format(தளை, அளவு) for தளை, அளவு in இறங்குவரிசை if அளவு)


class தமிழில்லா_உள்ளீட்டு_வரி:

    def __init__(தான், உள்ளீட்டு_வரி):
        தான்.உள்ளீட்டு_வரி = உள்ளீட்டு_வரி

    def __bool__(தான்):
        return False  # இது பா அல்ல

    def __repr__(தான்):
        return "தமிழில்லா வரி: " + தான்.உள்ளீட்டு_வரி


class பாக்கள்(list):
    """
    உள்ளீட்டிலிருந்து பாக்களைப் பிரித்து வைக்கவும் வெளியீட்டுக்காக அவற்றை str.format() செய்யவும் இந்த வகை பயன்படுகிறது
    """

    def __init__(தான், உள்ளீடு):

        if type(உள்ளீடு) is not str:
            raise TypeError("‘பாக்கள்’ பொருளை உருவாக்க ஒரு str பொருளை உள்ளிடவும்")

        super().__init__()
        அடி_கொத்து = []
        கடந்த_சீர் = None

        for அடி_ஒப்பு in அடி_வடிவம்.finditer(உள்ளீடு):
            உள்ளீட்டு_வரி = அடி_ஒப்பு.group(0)
            if உள்ளீட்டு_வரி[0] != "#" and அசை_வடிவம்.search(உள்ளீட்டு_வரி):  # வரியின் தொடக்கத்தில் # இல்லாது தமிழ் எழுத்துறுப்புகள் இருந்தால் அடி என்று கொள்க
                அ = அடி(உள்ளீட்டு_வரி, கடந்த_சீர்)
                அடி_கொத்து.append(அ)
                கடந்த_சீர் = அ[-1]  # இவ்வடியின் இறுதிச்சீர் அடுத்த அடிக்குக் கடந்த சீர்
            else:  # தமிழ் எழுத்துறுப்புகள் இல்லாத வரி; பா முற்றிற்று என்று கொள்க
                if அடி_கொத்து:
                    தான்.append(பா(அடி_கொத்து))
                    அடி_கொத்து = []
                    கடந்த_சீர் = None
                else:  # ஒன்றுக்கும் மேற்பட்ட தமிழில்லாத வரிகள்
                    தான்.append(தமிழில்லா_உள்ளீட்டு_வரி(உள்ளீட்டு_வரி))

        தான்.append(பா(அடி_கொத்து))

    def __repr__(தான்):
        return "\n\n".join(str(பா) for பா in தான் if பா)
        # இரட்டை வெற்று வரிகள் ஒரு வெற்றுப்பாவாக உட்கொள்ளப்படுவதால் if len(பா) என்பதைச் சேர்த்தோம்
        # ஒரு உள்ளீட்டுக்கு நேராக வெற்று வரிகள் உள்பட அதே அளவு வரிகள் கொண்ட ஆய்வைத் தேவையானால்
        # வெளியிடவே வெற்றுப்பாக்களைச் சேமித்தோம். இத்தகைய பயன்பாட்டை ‘பாவை’ மென்பொருளில் பார்க்கலாம்.
        # இந்த உள்விவரம் பிறகு மாறலாம் ஆனால் __repr__ வின் வெளியீடு மாறாது.
