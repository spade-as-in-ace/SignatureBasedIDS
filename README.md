# SignatureBasedIDS
<p><span style="color:green"> 7828251209993928209481656877199831537123138102782442818196230711117574281772633485046180053074128263285242774312721146492131514863315130781696865592425924593496359909828244019509108937257247511790416655189403975287685365661325098402469123974249643263557281448469092448414651133762880496461292921801964114926235841110754518504380918265130171755166469372942416814227371424197804710274326652141527103260505479163162749095141935032570186962896233831971176772167925478200713047129460184511147621958358225119280463103415359131295706421135541956415293101782565525081289959961535128552323572414115755301135084199442688226022186382892231422304916953270419521786765630389223552658315232357</span></p>

## Sig-Mal Project
The purpose of this project is to creat a signature-based intrusion-detection-system.\
The project will likely take the form of a Python script that can be called to analyze any offending file/executable and compare its signature against a known list of malware signatures.

## Technical Details
This follows a simple process. First the application will generate an MD5 hash on the specified target file. Then, the hash is checked against a list of known hashes. If it is found in the list, VirusTotal is consulted for further details on the piece of malware. As of now, only the MD5 hash is used.

## Technical Limitations
* In the python3-prototype it doesn't take memory into consideration when calculating the hash of the file. Thus this can use a lot of memory when working with larger files.
    * [This stackoverflow offers a solution to the problem](https://stackoverflow.com/questions/22058048/hashing-a-file-in-python)
