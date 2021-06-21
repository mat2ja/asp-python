# 3. Upotrebom mape napišite program koji daje riječ koja se najčešće pojavljuje u nekom
# zadanom tekstu. Možete iskoristiti program iz zadatka 1.


def najcesca_rijec(tekst):
    rijeci = tekst.split(" ")
    freq = {n: rijeci.count(n) for n in rijeci}

    keys = list(freq.keys())
    values = list(freq.values())
    return keys[values.index(max(values))]


def najcesca_rijec2(tekst):
    rijeci = tekst.split(" ")
    freq = {n: rijeci.count(n) for n in rijeci}
    return max(freq, key=freq.get)


def najcesca_rijec3(tekst):
    rijeci = tekst.split(" ")
    freq = {n: rijeci.count(n) for n in rijeci}
    naj = max(freq.values())
    naj_rijeci = list(filter(lambda k: freq[k] == naj, freq.keys()))
    return naj_rijeci[0] if len(naj_rijeci) <= 1 else naj_rijeci


def najcesca_rijec4(tekst):
    rijeci = tekst.split()
    for i in range(len(rijeci)):
        rijeci[i] = rijeci[i].lower()
        rijeci[i] = rijeci[i].replace(".", "")

    freq = {rijec: rijeci.count(rijec) for rijec in rijeci}

    naj = 0
    max_rijec = ""
    for k, v in freq.items():
        if v > naj:
            naj = v
            max_rijec = k

    return max_rijec


tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut placerat ante a lectus mollis facilisis. Nam ipsum justo, lobortis non metus viverra, sollicitudin tincidunt ligula. Vivamus consequat mattis tellus et tincidunt. Mauris pharetra et felis id consectetur. Praesent pulvinar magna eget elementum lacinia. Aenean arcu urna, blandit eu odio eu, semper dignissim dolor. Nulla in consequat mattis magna, sit amet ultrices mi ullamcorper et. Aenean sit amet purus orci. Nunc bibendum dolor sed egestas tristique. Ut commodo nulla augue, ut accumsan risus facilisis sed. Integer vitae cursus urna. Ut euismod felis in tortor faucibus, nec condimentum mauris faucibus. In consectetur massa at lobortis convallis. Proin eleifend purus vel semper pretium. Quisque ornare orci sodales, vehicula lacus ac, pellentesque dui. Sed enim diam, suscipit eu mollis vel, auctor at tortor. Maecenas quis mauris turpis. Pellentesque in pretium dolor, sit amet aliquet magna. Quisque in viverra sapien. Praesent rutrum diam consectetur viverra facilisis. Suspendisse vitae elementum justo. Aliquam felis sapien, euismod id nulla ultrices, vestibulum sagittis nisi. Aliquam consectetur aliquam ipsum, id hendrerit nulla dignissim sed. Vivamus dictum tellus vel gravida rutrum. Nunc tincidunt, metus at efficitur egestas, quam lectus mattis dolor, eu vulputate enim nisl id sapien. Integer justo ipsum, imperdiet eget nulla nec, imperdiet vulputate est. Sed quis arcu vel urna eleifend tempor vitae eget nisi. Aenean sodales leo risus, quis dapibus sapien dapibus eget. Cras tincidunt ante at fermentum malesuada. Nulla vulputate, turpis sed sagittis lacinia, tortor magna condimentum odio, id venenatis magna nulla id lacus. Duis egestas egestas enim eget sagittis. Curabitur luctus dolor in leo lacinia blandit. Nam lobortis maximus rutrum. Vestibulum mollis, augue ut vehicula scelerisque, elit massa gravida quam, id pellentesque risus augue commodo quam. Nam gravida hendrerit aliquam. Vivamus egestas sapien non sem aliquet fringilla. Phasellus eu condimentum enim. Aenean quis ante lectus. Vestibulum et dolor id metus viverra venenatis. Fusce velit arcu, lacinia eget mattis tristique, molestie at tellus. Donec facilisis at metus at vestibulum. In hac habitasse platea dictumst. Praesent ultrices diam sed interdum efficitur. Aenean mollis blandit elit cursus sodales. In egestas nulla eu felis fringilla, eu dignissim risus tincidunt. Sed lacinia nunc nisi, non mattis nulla condimentum ac. Nam sed orci auctor, ultrices lectus quis, ultrices ex. Cras ultricies semper neque nec tristique. Cras commodo felis et sapien vehicula, et semper massa blandit. Praesent commodo egestas lacus vel dapibus. Nunc tristique malesuada accumsan. Cras tincidunt pulvinar felis, lacinia euismod dolor pretium sed. Etiam maximus sapien sit amet velit molestie, vitae lacinia tortor lacinia. Proin suscipit vehicula imperdiet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vestibulum id nulla pulvinar, facilisis elit quis, rhoncus nisl. Etiam venenatis est sem, sed aliquam sem finibus in . Praesent sit amet odio lectus. Aliquam varius erat ac nibh luctus, ut bibendum eros egestas. Cras convallis hendrerit risus, quis ullamcorper odio aliquam eu. Donec faucibus sit amet neque sed dictum. Suspendisse aliquam dictum finibus. Donec in odio sed justo pellentesque facilisis quis a dolor. Curabitur suscipit, est quis tempor aliquam, nisl metus iaculis nunc, eu viverra urna tellus non tellus. Ut in ligula ut elit ullamcorper dignissim tristique quis mauris."

print(najcesca_rijec(tekst))
print(najcesca_rijec2(tekst))
print(najcesca_rijec3(tekst))
print(najcesca_rijec4(tekst))
