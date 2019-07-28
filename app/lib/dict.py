def load_dict():
    target_dict = {
        'bahasa' : 0,
        'kitab' : 1,
        'allah' : 2,
        'arsy' : 3,
        'agama' : 4,
        'petir' : 5,
        'guntur' : 6,
        'hujan' : 7,
        'awan' : 8,
        'angin' : 9,
        'arab' : 10,
        'warna' : 11,
        'hijau' : 12, 
        'merah' : 13,
        'biru' : 14,
        'hitam' : 15,
        'putih' : 16,
        'minyak' : 17,
        'karang' : 18,
        'tanah' : 19,
        'mutiara' : 20,
        'kaca' : 21,
        'debu' : 22,
        'sutra' : 23,
        'tanah liat' : 24,
        'besi' : 25,
        'emas' : 26,
        'perak' : 27,
        'kuningan' : 28, #
        'permata' : 29,
        'senjata' : 30,
        'dirham' : 31,
        'tinta' : 32,
        'pena' : 33,
        'tabut' : 34,
        'perahu' : 35,
        'kapal' : 36,
        'lampu' : 37,
        'kunci' : 38,
        'tangga' : 39,
        'bahtera' : 40,
        'masjid' : 41,
        'gereja' : 42,
        'biara' : 43, #
        'masjidil haram' : 44, #
        'masjidil aqsha' : 45, #
        'kabah' : 46, #
        'pisau' : 47,
        'panah' : 48,
        'baju besi' : 49,
        'tubuh' : 50,
        'badan' : 51,
        'penyakit' : 52,
        'sakit' : 53,
        'makanan' : 54,
        'janin' : 55,
        'darah' : 56,
        'tulang' : 57,
        'telinga' : 58,
        'mata' : 59,
        'jari' : 60,
        'dahi' : 61,
        'ubun ubun' : 62, #
        'jantung' : 63, #
        'hati' : 64, #
        'dada' : 65, #
        'punggung' : 66, #
        'tangan' : 67, #
        'kaki' : 68, #
        'perut' : 69, #
        'lambung' : 70, #
        'rambut' : 71, #
        'kulit' : 72, #
        'leher' : 73, #
        'dagu' : 74, #
        'tumit' : 75, #
        'usus' : 76, #
        'bibir' : 77, #
        'hidung' : 78, #
        'lidah' : 79, #
        'sayap' : 80, #
        'rusuk' : 81, #
        'kusta' : 82, #
        'daging' : 83, #
        'madu' : 84, #
        'susu' : 85, #
        'garam' : 86, #
        'roti' : 87, #
        'khamar' : 88, #
        'gandum' : 89, #
        'daging babi' : 90, #
        'bangkai' : 91, #
        'burung' : 92, #
        'tanaman' : 93, 
        'binatang' : 94,
        'ikan' : 95,
        'belalang' : 96, 
        'lebah' : 97, #
        'laba laba' : 98, #
        'semut' : 99,
        'kutu' : 100, #
        'nyamuk' : 101, #
        'lalat' : 102, #
        'gagak' : 103, #
        'salwa' : 104, #
        'hud hud' : 105, 
        'kebun' : 106,
        'mentimun' : 107, #
        'kurma' : 108, #
        'tin' : 109, #
        'jahe' : 110, #
        'anggur' : 111, #
        'sayur' : 112, #
        'daun' : 113, #
        'kelopak' : 114, #
        'mayang': 115, #
        'zaitun' : 116, #
        'bawang' : 117,
        'kacang' : 118, #
        'pohon' : 119,
        'delima' : 120, #
        'unta' : 121,
        'sapi' : 122,
        'babi' : 123, #
        'kambing' : 124,
        'kuda' : 125,
        'singa' : 126, #
        'keledai' : 127, #
        'bagal' : 128, #
        'kera' : 129, #
        'serigala' : 130, #
        'katak' : 131, #
        'domba' : 132, #
        'ular' : 133, #
        'anjing' : 134, #
        'malaikat' : 135,
        'jin' : 136,
        'manusia' : 137,
        'binatang melata' : 138, # 
        'jibril' : 139,
        'malaikat maut' : 140,
        'harut' : 141,
        'marut' : 142,
        'malik' : 143, 
        'mikail' : 144,
        'syaitan' : 145,
        'iblis' : 146,
        'raja' : 147,
        'anak adam' : 148,
        'nabi' : 149, 
        'firaun' : 150,
        'uzair' : 151,
        'luqman' : 152,
        'jalut' : 152,
        'dzulkifli' : 153,
        'samiri' : 154,
        'thalut' : 155,
        'karun' : 156,
        'dzulkarnain' : 157,
        'haman' : 158,
        'aad' : 159,
        'tsamud' : 160,
        'madyan' : 161,
        'quraisy' : 162,
        'romawi' : 163, 
        'anshar' : 164,
        'badui' : 165, 
        'tubba' : 166,
        'bani israil' : 167,
        'yajuj' : 168,
        'majuj' : 169,
        'orang yang mendiami gua' : 170,
        'tentara bergajah' : 171,
        'orang yang membuat parit' : 172,
        'penduduk rass' : 173,
        'penduduk aikah' : 174,
        'al hijr' : 175, 
        'abu lahab' : 176,
        'rasul' : 177,
        'zakaria' : 178,
        'yahya' : 179, 
        'harun' : 180,
        'idris' : 181,
        'ilyasa' : 182,
        'ayyub' : 183,
        'adam' : 184,
        'daud' : 185, 
        'sulaiman' : 186,
        'yusuf' : 187,
        'yaqub' : 188,
        'ishaq' : 189,
        'habil' : 190,
        'qabil' : 191,
        'israil' : 192,
        'aazar' : 193,
        'muhammad' : 194,
        'isa' : 195,
        'ibrahim' : 196,
        'ismail' : 197,
        'shaleh' : 198,
        'hud' : 199,
        'syuaib' : 200,
        'yunus' : 201,
        'musa' : 202,
        'nuh' : 203,
        'luth' : 204,
        'ilyas' : 205,
        'ahmad' : 206,
        'zaid' : 207,
        'maryam' : 208,
        'al masih' : 209,
        'quran' : 210,
        'injil' : 211,  
        'zabur' : 212,
        'taurat' : 213,
        'islam' : 214,
        'nasrani' : 215,
        'yahudi' : 216,
        'shabiin' : 217,
        'majusi' : 218,
        'bulan' : 219,
        'bumi' : 220,
        'matahari' : 221, #
        'bintang' : 222,
        'syira' : 223, #
        'gugusan bintang' : 224,
        'al uzza' : 225, #
        'manat' : 226, #
        'al lata' : 227,
        'suwwa' : 228, #
        'baal' : 229, #
        'nasr' : 230, #
        'wadd' : 231, #
        'yaghuts' : 232, #
        'yauq' : 233, #
        'berhala' : 234,
        'lembu' : 235, #
        'akhirat' : 236,
        'jahiliyah' : 237, #
        'jumat' : 238,
        'sabtu' : 239,
        'haji' : 240,
        'umrah' : 241,
        'malam kemuliaan' : 242, #
        'ramadhan' : 243, 
        'fajar' : 244, #
        'kebangkitan' : 245,
        'hari kiamat' : 246,
        'surga' : 247,
        'neraka' : 248,
        'firdaus' : 249,
        'adn' : 250,
        'pohon bidara' : 251,
        'salsabil' : 252,
        'sijjin' : 253,
        'saqar' : 254,
        'zaqqum' : 255,
        'api yang bergejolak' : 257, #
        'ufuk' : 258, #
        'kiblat' : 259,
        'dusun' : 260, #
        'kota' : 261,
        'gunung' : 262,
        'badar' : 263,
        'mekah' : 264,
        'baitullah' : 265, #
        'madinah' : 267, #
        'babil' : 268,
        'hunain' : 269,
        'iram' : 270,
        'yastrib' : 271, #
        'shafa' : 272, 
        'marwa' : 273, 
        'arafah' : 274,
        'sinai' : 275, 
        'bukit judi' : 276,
        'mesir' : 277,
        'saba' : 278,
        'al ahqaf' : 279,
        'imran' : 280,
        'keluarga' : 281, # --------
        'ayah' : 282,
        'ibu' : 283,
        'bapak' : 284,
        'anak' : 285,
        'yatim' : 286,
        'saudara' : 287,
        'budak' : 288,
        'laki' : 289,
        'perempuan' : 290,
        'harta' : 291,
        'niaga' : 292,
        'jual beli' : 293,
        'hutang' : 294,
        'riba' : 295,
        'dagang' : 296,
        'ibadah' : 297,
        'shalat' : 298,
        'puasa' : 299,
        'zakat' : 300,
        'sedekah' : 301,
        'negara' : 302,
        'bangsa' : 303,
        'hukum' : 304,
        'adil' : 305,
        'kisah' : 306,
        'hikmah' : 307,
        'ilmu' : 308,
        'perang' : 309,
        'zalim' : 310
    }

    # 'bahasa','kitab','allah','arsy','agama','petir','guntur','hujan','awan','angin','arab','warna','hijau','merah','biru','hitam','putih','minyak','karang', 'tanah','mutiara','kaca','debu','sutra','tanah liat','besi','emas','perak','kuningan','permata','senjata','dirham','tinta','pena','tabut','perahu','kapal','lampu','kunci','tangga','bahtera','masjid','gereja','biara','masjidil haram','masjidil aqsha','kabah','pisau','panah','baju besi','tubuh','badan','penyakit','sakit','makanan','janin','darah','tulang','telinga','mata','jari','dahi','ubun ubun','jantung','hati','dada','punggung','tangan','kaki','perut','lambung','rambut','kulit','leher','dagu','tumit','usus','bibir','hidung', 'lidah','sayap','rusuk','kusta','daging','madu','susu','garam','roti','khamar','gandum','daging babi','bangkai','burung','tanaman','binatang','ikan','belalang','lebah','laba laba','semut','kutu','nyamuk','lalat','gagak','salwa','hud hud','kebun','mentimun','kurma','tin','jahe','anggur','sayur','daun','kelopak','mayang','zaitun','bawang','kacang','pohon','delima','unta','sapi','babi','kambing','kuda','singa','keledai','bagal','kera','serigala','katak','domba','ular','anjing','malaikat','jin','manusia','binatang melata','jibril','malaikat maut','harut','marut','malik','mikail','syaitan','iblis','raja','anak adam','nabi','firaun','uzair','luqman','jalut','zulkifli','samiri','thalut','karun','dzulkarnain','haman','aad','tsamud','madyan', 'quraisy','romawi','anshar','badui','tubba','bani israil','yajuj','majuj','orang yang mendiami gua','tentara bergajah','orang yang membuat parit','penduduk rass','penduduk aikah','al hijr','abu lahab','rasul','zakaria','yahya','harun','idris','ilyasa','ayyub','adam','daud','sulaiman','yusuf','yaqub','ishaq','habil','qabil','israil','aazar','muhammad','isa','ibrahim','ismail','shaleh','hud','syuaib','yunus','musa','nuh','luth','ilyas','ahmad','zaid','maryam','al masih','quran','injil','zabur','taurat','islam','nasrani','yahudi','shabiin','majusi','bulan','bumi','matahari','bintang','syira','gugusan bintang','al uzza','manat','al lata','suwwa','baal','nasr','wadd','yaghuts','yauq','berhala','lembu','akhirat','jahiliyah','jumat','sabtu','haji', 'umrah','malam kemuliaan','ramadhan','fajar','kebangkitan','hari kiamat','surga','neraka','firdaus','adn','pohon bidara','salsabil','sijjin','saqar','zaqqum','api yang bergejolak','ufuk','kiblat','dusun','kota','gunung','badar','mekah','baitullah','madinah','babil','hunain','iram','yastrib','shafa','marwa','arafah','sinai','bukit judi','mesir','saba','al ahqaf','imran','keluarga','ayah','ibu','bapak','anak','yatim','saudara','budak','laki','perempuan','harta','niaga','jual beli','hutang','riba','dagang','ibadah','shalat','puasa','zakat','sedekah','negara','bangsa','hukum','adil','kisah','hikmah','ilmu','perang','zalim'

    surah_dict = {
        '1' : 'Al-Fatihah',
        '2' : 'Al-Baqarah',
        '3' : 'Ali Imran',
        '4' : 'An-Nisaa\'',
        '5' : 'Al-Maa\'idah',
        '6' : 'Al-An\'am',
        '7' : 'Al-A\'raf',
        '8' : 'Al-Anfaal',
        '9' : 'At-Taubah',
        '10' : 'Yunus',
        '11' : 'Hud',
        '12' : 'Yusuf',
        '13' : 'Ar-Ra\'d',
        '14' : 'Ibrahim',
        '15' : 'Al-Hijr',
        '16' : 'An-Nahl',
        '17' : 'Al-Israa\'',
        '18' : 'Al-Kahfi',
        '19' : 'Maryam',
        '20' : 'Ta-Ha',
        '21' : 'Al-Anbiyaa\'',
        '22' : 'Al-Hajj',
        '23' : 'Al-Mu\'minun',
        '24' : 'An-Nuur',
        '25' : 'Al-Furqan',
        '26' : 'Asy-Syu\'ara',
        '27' : 'An-Naml',
        '28' : 'Al-Qasas',
        '29' : 'Al-Ankabut',
        '30' : 'Ar-Ruum',
        '31' : 'Luqman',
        '32' : 'As-Sajdah',
        '33' : 'Al-Ahzab',
        '34' : 'Sabaa\'',
        '35' : 'Fatir',
        '36' : 'Yasin',
        '37' : 'As-Saffaat',
        '38' : 'Shad',
        '39' : 'Az-Zumar',
        '40' : 'Ghaafir',
        '41' : 'Fussilat',
        '42' : 'Asy-Syura\'',
        '43' : 'Az-Zukhruf',
        '44' : 'Ad-Dukhan',
        '45' : 'Al-Jaasiyah',
        '46' : 'Al-Ahqaf',
        '47' : 'Muhammad',
        '48' : 'Al-Fath',
        '49' : 'Al-Hujurat',
        '50' : 'Qaf',
        '51' : 'Adz-Dzariyat',
        '52' : 'At-Tuur',
        '53' : 'An-Najm',
        '54' : 'Al-Qomar',
        '55' : 'Ar-Rahman',
        '56' : 'Al-Waqi\'ah',
        '57' : 'Al-Hadid',
        '58' : 'Al-Mujadilah',
        '59' : 'Al-Hasyr',
        '60' : 'Al-Mumtahanah',
        '61' : 'As-Saff',
        '62' : 'Al-Jumu\'ah',
        '63' : 'Al-Munafiqun',
        '64' : 'At-Taghabun',
        '65' : 'At-Talaq',
        '66' : 'At-Tahrim',
        '67' : 'Al-Mulk',
        '68' : 'Al-Qolam',
        '69' : 'Al-Haqqah',
        '70' : 'Al-Ma\'arij',
        '71' : 'Nuh',
        '72' : 'Al-Jinn',
        '73' : 'Al-Muzammil',
        '74' : 'Al-Muddatsir',
        '75' : 'Al-Qiyamah',
        '76' : 'Al-Insan',
        '77' : 'Al-Mursalat',
        '78' : 'An-Naba',
        '79' : 'An-Nazi\'at',
        '80' : '\'Abasa',
        '81' : 'At-Takwir',
        '82' : 'Al-Infitar',
        '83' : 'Al-Muthaffifin',
        '84' : 'Al-Insyiqaq',
        '85' : 'Al-Buruj',
        '86' : 'At-Thariq',
        '87' : 'Al-A\'la',
        '88' : 'Al-Ghasiyah',
        '89' : 'Al-Fajr',
        '90' : 'Al-Balad',
        '91' : 'Asy-Syams',
        '92' : 'Al-Lail',
        '93' : 'Ad-Dhuha',
        '94' : 'Al-Insyirah',
        '95' : 'At-Tin',
        '96' : 'Al-Alaq',
        '97' : 'Al-Qadr',
        '98' : 'Al-Bayyinah',
        '99' : 'Az-Zalzalah',
        '100' : 'Al-Adiyat',
        '101' : 'Al-Qariah',
        '102' : 'At-Takatsur',
        '103' : 'Al-Asr',
        '104' : 'Al-Humazah',
        '105' : 'Al-Fiil',
        '106' : 'Quraisy',
        '107' : 'Al-Maun',
        '108' : 'Al-Kautsar',
        '109' : 'Al-Kafirun',
        '110' : 'An-Nasr',
        '111' : 'Al-Masad',
        '112' : 'Al-Ikhlas',
        '113' : 'Al-Falaq',
        '114' : 'An-Nas'
    }
    
    return target_dict, surah_dict