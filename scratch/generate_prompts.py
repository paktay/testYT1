# -*- coding: utf-8 -*-
prompts = [
    # 1. (0:00) Di lantai 27 sebuah gedung pencakar langit di Dallas, Texas, bulan September tahun 2000.
    "Isometric 3D cutaway diorama of an executive boardroom on the 27th floor of a sleek Dallas skyscraper, September 2000. Through panoramic glass windows, a miniature clay skyline of Dallas basks in warm late-afternoon sunlight. Inside features a polished mahogany conference table, leather swivel chairs, retro year-2000 office decor, CRT desktop computer, and architectural blueprints. Handcrafted claymation aesthetic, textured plasticine finish with subtle fingerprint details, soft studio lighting, tilt-shift depth of field --ar 16:9 --v 6.1",

    # 2. (0:07) Suasananya begitu dingin dan tegang.
    "Isometric 3D claymation scene of a high-rise executive conference room filled with cold, tense atmosphere. Dramatic cool-toned blue shadows, dim cinematic lighting, an imposing mahogany boardroom table reflecting long sharp shadows. Empty coffee cups and unopened folders, air thick with corporate tension. Handcrafted plasticine textures, subtle clay imperfections, volumetric studio rim lighting, tilt-shift miniature diorama --ar 16:9 --v 6.1",

    # 3. (0:10) Tiga orang pria masuk ke ruangan dengan kemeja yang masih kusut setelah penerbangan murah dari California.
    "Isometric 3D clay diorama of three tired men entering a luxury executive boardroom. They wear wrinkled short-sleeved dress shirts and slightly loosened ties, carrying scuffed leather messenger bags after a cramped budget flight from California. Handcrafted claymation figures with expressive weary faces, plasticine texture, warm office floor lamps contrasting with their fatigued postures, tilt-shift 3D render --ar 16:9 --v 6.1",

    # 4. (0:18) Mereka adalah Reed Hastings, Mark Randolph, dan direktur keuangan mereka, Barry McCarthy.
    "Isometric 3D claymation character trio standing together inside a corporate office: miniature clay figures of Reed Hastings with his signature goatee, Marc Randolph holding a business notebook, and CFO Barry McCarthy holding financial ledger binders. Stylized plasticine clay models, detailed wrinkled fabric texture on their business shirts, soft directional spotlight, miniature handcrafted diorama aesthetic --ar 16:9 --v 6.1",

    # 5. (0:25) Di seberang meja rapat panjang berlapis kayu mahoni, duduk pria paling berkuasa di industri hiburan rumahan dunia saat itu,
    "Isometric 3D cutaway view of an opulent executive suite. Across a massive gleaming mahogany conference table sits a commanding corporate titan like a king on his throne. Polished marble flooring, gold-trimmed clay pen sets, high-end office luxury, low-angle perspective emphasizing authority and power. Handcrafted claymation, rich plasticine textures, warm golden studio lighting, tilt-shift miniature render --ar 16:9 --v 6.1",

    # 6. (0:33) John Antioco, CEO Blockbuster.
    "Isometric 3D claymation portrait of John Antioco, CEO of Blockbuster, seated at the head of a massive conference desk. A distinguished miniature clay man with slicked silver-streaked hair, wearing a pristine navy bespoke tailored pinstripe suit and silk tie, oozing absolute authority and confidence. Handcrafted plasticine details, soft key lighting, tilt-shift focus, stylized miniature figurine --ar 16:9 --v 6.1",

    # 7. (0:36) Antioco mengenakan stelan jazz bispok mahal, bersandar-santai di kursinya.
    "Isometric 3D clay diorama of CEO John Antioco reclining comfortably deep into an oversized black leather executive armchair. Legs relaxed, arms resting smoothly on mahogany armrests, holding an expensive fountain pen with nonchalant composure. Ambient high-rise sunlight casting sleek reflections on polished wood. Textured plasticine clay, soft studio lighting, tilt-shift miniature aesthetic --ar 16:9 --v 6.1",

    # 8. (0:42) Di belakang punggungnya berdiri sebuah kerajaan bernilai 6 miliar dolar,
    "Isometric 3D symbolic claymation diorama: behind an executive leather chair stands a colossal towering corporate fortress monument labeled with golden clay numbers '$6,000,000,000'. Stacks of miniature clay money bricks and golden corporate pillars soaring skyward, representing an untouchable retail empire. Handcrafted plasticine, dramatic theatrical spotlight, tilt-shift render --ar 16:9 --v 6.1",

    # 9. (0:47) 9 ribu toko di seluruh penjuru bumi, dan puluhan juta pelanggan setia.
    "Isometric 3D miniature clay globe floating gently, dotted with thousands of tiny iconic blue-and-yellow Blockbuster retail stores across continents. Swarms of cheerful miniature clay shoppers carrying plastic rental bags, representing tens of millions of loyal customers worldwide. Handcrafted claymation aesthetic, vibrant plasticine colors, soft global studio lighting, tilt-shift diorama --ar 16:9 --v 6.1",

    # 10. (0:51) Sedangkan tiga tamunya dari California, mereka hanyalah pendiri startup kecil bernama Netflix
    "Isometric 3D clay cutaway diorama showing a stark contrast: three modest clay startup founders holding small red paper DVD envelopes, standing opposite a towering wall of corporate luxury. Tiny logo on their envelopes reads 'Netflix'. Handcrafted plasticine clay style, fragile startup energy versus massive corporate hegemony, soft directional lighting, miniature diorama --ar 16:9 --v 6.1",

    # 11. (0:58) yang baru saja babak belur dihantam badai.com crash.
    "Isometric 3D clay diorama of a chaotic tech startup office during the dot-com crash of 2000. Stormy miniature clay clouds raining lightning over broken CRT computer monitors, tumbling red financial graph arrows, scattered papers on the floor, stressed clay workers trying to brace falling shelves. Textured plasticine, moody dynamic lighting, tilt-shift miniature render --ar 16:9 --v 6.1",

    # 12. (1:03) Pelanggan mereka baru sekitar 300 ribu orang,
    "Isometric 3D clay diorama of a small cluster of clay customers standing beside a modest red-and-white postal mailbox kiosk. An illuminated retro digital counter board displays the number '300,000 Subscribers'. Handcrafted claymation aesthetic, intimate miniature scale, cozy neighborhood setting, soft warm morning lighting, tilt-shift focus --ar 16:9 --v 6.1",

    # 13. (1:06) dan di tahun itu saja mereka diproyeksikan merugi hampir 60 juta dolar.
    "Isometric 3D claymation financial scene: a steep downward-sloping red clay chart plummeting off an executive desk into a warning red zone marked '-$60,000,000 Loss'. Distressed miniature clay founders staring with anxious expressions at financial balance sheets. Handcrafted plasticine textures, dramatic warning red and cool blue lighting, tilt-shift diorama --ar 16:9 --v 6.1",

    # 14. (1:12) Kas mereka hampir ludes.
    "Isometric 3D cutaway diorama of an open corporate metal safe, almost completely empty. Only three small clay coins and a tiny cobweb remain on the bottom shelf, symbolizing near-total cash exhaustion. Handcrafted claymation style, tactile plasticine surface, dramatic single beam of spotlight cutting through shadows, tilt-shift depth of field --ar 16:9 --v 6.1",

    # 15. (1:14) Dengan napas tertahan, Reed Hastings menyodorkan satu angka di atas meja,
    "Isometric 3D claymation close-up at a mahogany table: miniature clay hands of Reed Hastings cautiously sliding a crisp white contract folder across the reflective wood grain, holding his breath with tense posture. Ambient high-rise window light glistening on the paper edge. Handcrafted plasticine, subtle finger textures, cinematic suspense lighting, tilt-shift focus --ar 16:9 --v 6.1",

    # 16. (1:19) 50 juta dolar.
    "Isometric 3D macro clay diorama of a single legal proposal document lying flat on dark mahogany wood. In bold embossed golden clay lettering across the center page reads '$50,000,000'. Clean corporate contract layout, handcrafted claymation texture with delicate plasticine edges, dramatic focused spotlight, shallow tilt-shift depth of field --ar 16:9 --v 6.1",

    # 17. (1:22) Rencananya sederhana.
    "Isometric 3D clay diorama of a clean, minimalist business whiteboard illustration. Handcrafted clay arrows connect a miniature blue Blockbuster retail shop to a miniature red Netflix delivery van, meeting in a golden handshake symbol. Elegant and straightforward strategic partnership blueprint, soft bright studio lighting, plasticine craft style --ar 16:9 --v 6.1",

    # 18. (1:23) Blockbuster membeli Netflix seharga 50 juta dolar,
    "Isometric 3D conceptual clay diorama: a massive blue-and-yellow Blockbuster retail store model acquiring and absorbing a sleek red Netflix postage box, with a golden price tag of '$50M' hanging between them. Handcrafted plasticine clay models, clean diorama platform, bright balanced studio lighting, tilt-shift miniature perspective --ar 16:9 --v 6.1",

    # 19. (1:27) dan sebagai gantinya, tim Netflix akan mengelola divisi online Blockbuster yang masih tertatih-tatih.
    "Isometric 3D cutaway diorama of a tech server room: three energetic clay Netflix techies in wrinkled shirts eagerly fixing, rewiring, and modernizing a dusty, sluggish Blockbuster online server rack with glowing optical cables. Handcrafted claymation aesthetic, colorful wiring, glowing LEDs, soft futuristic studio lighting, tilt-shift diorama --ar 16:9 --v 6.1",

    # 20. (1:34) Ruangan mendadak hening beberapa detik.
    "Isometric 3D claymation scene of an executive boardroom suddenly frozen in dead silence. An antique analog pendulum clock on the wall ticks motionless, dust motes suspended in sunbeams, corporate executives frozen mid-breath around the table. Handcrafted plasticine clay, moody dramatic stillness, high contrast lighting, tilt-shift miniature render --ar 16:9 --v 6.1",

    # 21. (1:37) John Antioco menatap berkas itu, menatap tiga pria di depannya,
    "Isometric 3D clay diorama showing CEO John Antioco looking down with a sharp gaze at the $50M proposal folder, then lifting his eyes to scrutinize the three humble startup founders across the table. Heavy tension in the air, expressive sculpted clay faces, sleek corporate boardroom environment, soft warm rim lighting, tilt-shift depth of field --ar 16:9 --v 6.1",

    # 22. (1:42) lalu bersandar lebih dalam ke kursinya.
    "Isometric 3D claymation figure of John Antioco sinking further back into his luxurious high-backed leather chair, steepling his clay fingers with a patronizing smirk, tilting his head with condescending amusement. Handcrafted plasticine suit folds, deep leather chair cushioning, crisp rim lighting, tilt-shift miniature view --ar 16:9 --v 6.1",

    # 23. (1:44) Para eksekutif Blockbuster yang mendampinginya mulai saling berbisik,
    "Isometric 3D clay diorama of sharp-suited Blockbuster vice presidents and executives seated alongside the table, leaning in close to whisper into each other's ears behind cupped hands. Subtle smirks and mocking glances exchanged. Handcrafted claymation, rich plasticine textures, soft office ceiling lighting, tilt-shift miniature aesthetic --ar 16:9 --v 6.1",

    # 24. (1:49) berusaha keras menahan senyum dan tawa sinis.
    "Isometric 3D claymation close-up of executive faces trying hard to stifle condescending giggles and cynical smirks. Cheeks puffed, lips bitten, hands muffling laughs across the mahogany boardroom table. Stylized expressive plasticine clay figures, humorous caricature aesthetic, warm studio lighting, tilt-shift focus --ar 16:9 --v 6.1",

    # 25. (1:53) Bagi mereka, angka 50 juta dolar untuk perusahaan rental post yang sedang sekarat adalah lelucon konyol.
    "Isometric 3D conceptual clay diorama: a small vintage clay postal mailcart carrying red DVD envelopes with a modest price tag of '$50 Million', juxtaposed against towering corporate executive clay figurines with skeptical and amused expressions. Whimsical business satire, handcrafted plasticine textures, theatrical warm spotlighting, tilt-shift miniature perspective --ar 16:9 --v 6.1",

    # 26. (2:01) Pertemuan selesai dalam hitungan menit.
    "Isometric 3D clay diorama of the rapid conclusion of a meeting. Corporate boardroom heavy oak double doors swinging open, briefcases snapped shut in haste, business folders packed away within minutes. Handcrafted claymation models, dynamic motion blur on closing door, cool office lighting, tilt-shift miniature render --ar 16:9 --v 6.1",

    # 27. (2:03) Tawaran itu ditolak mentah-mentah.
    "Isometric 3D claymation shot of the $50M proposal contract shoved dismissively back across the mahogany table with a firm clay hand gesture. Cold, unequivocal rejection. The paper slides off the edge into empty air. High drama, handcrafted plasticine clay textures, stark rim lighting, shallow depth of field --ar 16:9 --v 6.1",

    # 28. (2:06) Tapi sejarah punya cara yang kejam untuk menertawakan arogansi.
    "Isometric 3D symbolic clay diorama: an ornate classical clay statue symbolizing corporate hubris and arrogance, while a giant sculpted hand of father time turns a huge brass clock gear ominously in the background. Handcrafted plasticine style, theatrical chiaroscuro lighting, tilt-shift miniature aesthetic --ar 16:9 --v 6.1",

    # 29. (2:10) Tepat sepuluh tahun kemudian,
    "Isometric 3D clay diorama of a giant retro flip calendar standing in the center of an empty highway, rapid pages flipping dynamically forward through time from 'September 2000' to 'September 2010'. Motion-blurred calendar leaves made of clay, sunset golden hour lighting, tilt-shift miniature perspective --ar 16:9 --v 6.1",

    # 30. (2:13) kerajaan 6 miliar dolar milik John Antioco rata dengan tanah,
    "Isometric 3D claymation scene of complete corporate ruin: the once-mighty $6 billion Blockbuster empire building collapsed into cracked clay rubble, broken yellow-and-blue signboards lying shattered on cracked asphalt. Handcrafted plasticine textures, desolate overcast sky, soft post-apocalyptic studio lighting, tilt-shift diorama --ar 16:9 --v 6.1",

    # 31. (2:18) bangkrut dengan utang 1 miliar dolar.
    "Isometric 3D clay diorama of an oversized wooden judicial gavel slamming down onto a teetering mountain of unpaid invoices, red final notices, and court documents stamped 'Chapter 11 Bankruptcy - $1 Billion Debt'. Dust particles of clay exploding on impact, dramatic overhead spotlight, plasticine craft style --ar 16:9 --v 6.1",

    # 32. (2:22) Sementara dua pemuda berkemeja kusut yang ditertawakan hari itu,
    "Isometric 3D clay diorama of the two once-mocked founders standing tall on a rising cliff, holding a glowing crimson digital tablet, looking toward a bright technological sunrise. Their rumpled shirts now look visionary. Handcrafted claymation figures, inspiring golden sunrise lighting, tilt-shift perspective --ar 16:9 --v 6.1",

    # 33. (2:26) baru saja mengubah cara seluruh umat manusia di planet bumi menikmati tontonan.
    "Isometric 3D clay diorama of a global landscape at night: thousands of cozy miniature clay houses glowing warmly, each living room window illuminated by the soft red glow of a Netflix movie streaming on screen. Handcrafted plasticine houses, twinkling neighborhood lights, cozy midnight atmosphere, tilt-shift diorama --ar 16:9 --v 6.1",

    # 34. (2:32) Untuk memahami mengapa penolakan itu terjadi,
    "Isometric 3D clay diorama of an oversized vintage bronze magnifying glass hovering over an archival timeline chart and corporate blueprint, examining key historical turning points. Vintage research aesthetic, warm desk lamp illumination, intricate miniature clay documents, tilt-shift depth of field --ar 16:9 --v 6.1",

    # 35. (2:35) kita harus memundurkan jam ke era keemasan blockbuster di dekade 90-an.
    "Isometric 3D clay diorama featuring a nostalgic retro time machine dial turning backwards into the glorious 1990s. Neon synthwave pastel lights, glowing cassette tapes, vibrant nostalgic aesthetic. Handcrafted claymation textures, vibrant plasticine colors, warm neon glow, tilt-shift miniature render --ar 16:9 --v 6.1",

    # 36. (2:41) Jika Anda tumbuh di era itu,
    "Isometric 3D clay cutaway diorama of a cozy 1990s living room: floral fabric sofa, wood-paneled walls, a chunky CRT television playing a movie, and a carpet littered with VHS rental cases. Warm nostalgic Saturday evening vibe, handcrafted plasticine clay, cozy ambient indoor lighting, tilt-shift focus --ar 16:9 --v 6.1",

    # 37. (2:43) malam minggu hampir mustahil dilewati
    "Isometric 3D clay diorama of a cheerful suburban street on Saturday evening: stylish miniature clay figures boarding a classic vintage wood-sided station wagon under warm streetlamps, ready for an evening outing. Handcrafted claymation townscape, pleasant twilight glow, tilt-shift miniature perspective --ar 16:9 --v 6.1",

    # 38. (2:45) tanpa mengunjungi toko dengan logo sobekan tiket berwarna biru dan kuning tersebut.
    "Isometric 3D clay diorama of an iconic Blockbuster video store at night: glowing neon yellow and blue torn-ticket logo sign shining over glass storefront doors. Crowds of miniature clay families excitedly entering and exiting with plastic rental bags. Handcrafted plasticine textures, brilliant neon glow, tilt-shift perspective --ar 16:9 --v 6.1",

    # 39. (2:51) Blockbuster bukan sekedar bisnis retail.
    "Isometric 3D cutaway diorama of an organized retro 1990s movie rental shop interior: tidy rows of white display shelves filled with colorful miniature VHS tape boxes, a small checkout counter with popcorn buckets, soft ambient overhead lighting. Handcrafted claymation aesthetic, textured plasticine finish, clean miniature diorama, tilt-shift depth of field --ar 16:9 --v 6.1",

    # 40. (2:54) Mereka adalah budaya pop itu sendiri.
    "Isometric 3D clay collage diorama representing 1990s pop culture: a Blockbuster membership card, giant plastic tubs of buttery cinema popcorn, VHS rewinders shaped like sports cars, and neon movie candy boxes sculpted from colorful plasticine clay. Handcrafted claymation, festive studio lighting, tilt-shift focus --ar 16:9 --v 6.1",

    # 41. (2:57) Pada masa puncaknya,
    "Isometric 3D clay diorama of an enormous golden mountain peak rising high above the clouds, crowned with a giant gleaming blue-and-yellow Blockbuster flag, symbolizing the absolute pinnacle of retail dominance. Handcrafted plasticine clouds and stone, majestic sunrise lighting, tilt-shift miniature scale --ar 16:9 --v 6.1",

    # 42. (2:58) 60 persen populasi Amerika Serikat tinggal hanya dalam jarak 10 menit berkendara
    "Isometric 3D diorama of an American suburban regional map: a prominent circular radius zone indicating '10-Minute Drive' encircling a glowing blue Blockbuster store, covering 60% of surrounding clay neighborhoods. Handcrafted plasticine streets and houses, soft aerial studio lighting, tilt-shift render --ar 16:9 --v 6.1",

    # 43. (3:04) dari satu gerai blockbuster.
    "Isometric 3D clay diorama of a full retail parking lot outside a Blockbuster store: miniature colorful clay family cars cruising smoothly into parking spots under sodium-vapor streetlights, eager shoppers hopping out. Handcrafted plasticine models, twilight atmosphere, tilt-shift depth of field --ar 16:9 --v 6.1",

    # 44. (3:07) Mereka mempekerjakan 84 ribu orang di 9 ribu gerai di seluruh dunia.
    "Isometric 3D mega-diorama of a corporate network: an expansive grid platform showing miniature scale models of 9,000 blue retail outlets worldwide and swarms of 84,000 tiny clay employee figurines in blue polo shirts and khakis. Handcrafted claymation style, grand isometric view, balanced studio lighting --ar 16:9 --v 6.1",

    # 45. (3:13) Pendapatannya setara dengan industri film itu sendiri.
    "Isometric 3D clay diorama of a giant classical balance scale: on one brass tray sits a miniature Hollywood studio film reel lot, and on the other tray sits a towering stack of Blockbuster retail earnings, balanced in perfect equilibrium. Handcrafted plasticine, polished brass clay finish, dramatic theatrical lighting --ar 16:9 --v 6.1",

    # 46. (3:17) Namun di balik kesuksesan tak sasa itu,
    "Isometric 3D cutaway diorama showing two halves of a retro video store: on one side a brightly lit retail showroom with colorful movie shelves, and on the other side a quiet back-office filled with tall gray filing cabinets and analytical strategy charts. Dual-toned studio lighting, handcrafted claymation aesthetic, textured plasticine finish, tilt-shift miniature perspective --ar 16:9 --v 6.1",

    # 47. (3:20) tersimpan satu rahasia gelap yang jarang dibicarakan secara jujur.
    "Isometric 3D clay diorama of a heavily padlocked corporate vault hidden under the checkout counter, surrounded by whispered shadows and confidential ledgers of hidden penalties. Handcrafted plasticine textures, mysterious side-lighting cutting through dark shadows, tilt-shift depth of field --ar 16:9 --v 6.1",

    # 48. (3:24) Model bisnis blockbuster tidak dirancang untuk membuat penonton bahagia.
    "Isometric 3D claymation conceptual diorama: a cheerful customer maze made of retail video shelves that deceitfully funnels unsuspecting clay shoppers straight into a trap cage labeled 'Penalty Zone'. Handcrafted plasticine figures, ironic visual storytelling, warm yet cynical lighting, tilt-shift view --ar 16:9 --v 6.1",

    # 49. (3:30) Model bisnis mereka dirancang untuk menghukum penonton yang lalai.
    "Isometric 3D clay diorama of a large rolled-out corporate policy document on a polished wooden desk, viewed through an oversized magnifying glass pointing at fine print next to a classic hourglass. Handcrafted claymation aesthetic, crisp plasticine textures, focused desk spotlight, tilt-shift miniature perspective --ar 16:9 --v 6.1",

    # 50. (3:35) Nama instrumen itu adalah Late Fee,
    "Isometric 3D clay diorama featuring an ominous, oversized mechanical rubber stamp suspended in mid-air, carved with the bold warning words 'LATE FEE' dripping with thick red clay ink. Handcrafted claymation aesthetic, dramatic warning red spotlight, intense tilt-shift focus --ar 16:9 --v 6.1",

    # 51. (3:38) denda keterlambatan pengembalian kaset.
    "Isometric 3D clay cutaway diorama of an overdue black plastic VHS tape resting innocently on a dusty rug under a living room sofa, surrounded by floating dust bunnies and an ominous ticking digital clock. Handcrafted plasticine, moody floor-level lighting, tilt-shift miniature focus --ar 16:9 --v 6.1",

    # 52. (3:41) Di tahun 2000 saja,
    "Isometric 3D clay diorama of a corporate financial desk in the year 2000: an oversized desk calendar displaying 'Year 2000 Fiscal Summary' surrounded by golden abacuses and calculators made of plasticine clay. Handcrafted claymation, clean professional studio lighting, tilt-shift render --ar 16:9 --v 6.1",

    # 53. (3:43) blockbuster meraup 800 juta dolar bersih hanya dari denda keterlambatan.
    "Isometric 3D clay diorama of a towering colossal mountain of cash totaling $800,000,000 made of miniature green clay hundred-dollar bill bundles, topped with a banner reading 'Late Fee Profits'. Handcrafted plasticine texture, triumphant yet greedy golden lighting, tilt-shift miniature scale --ar 16:9 --v 6.1",

    # 54. (3:49) Mari kita cerna angka itu sejenak.
    "Isometric 3D clay diorama of two miniature clay analysts in business suits rubbing their chins in astonishment, gazing upward at the incomprehensible height of the $800 million late-fee cash mountain. Handcrafted claymation figures, humorous scale contrast, soft studio rim lighting, tilt-shift depth of field --ar 16:9 --v 6.1",

    # 55. (3:51) 800 juta dolar.
    "Isometric 3D clay macro shot: gigantic, monumental 3D clay numbers '$800,000,000' sculpted out of polished gold and green clay standing majestically on an executive stage under sharp spotlights. Handcrafted plasticine with smooth matte finish, cinematic theatrical lighting, tilt-shift focus --ar 16:9 --v 6.1",

    # 56. (3:54) Angka tersebut menyumbang 16 persen dari seluruh pendapatan tahunan perusahaan
    "Isometric 3D clay diorama of a massive circular corporate pie chart hovering above a boardroom table: an illuminated glowing orange slice representing 16% of total revenue glows intensely against the rest of the chart. Handcrafted plasticine textures, clean infographics in clay, soft studio lighting --ar 16:9 --v 6.1",

    # 57. (3:59) dan hampir mewakili seluruh marjin keuntungan bersih mereka.
    "Isometric 3D clay diorama of a sleek golden balance scale on a mahogany table: on one side rests a glowing orange 3D pie-chart wedge labeled '16%', perfectly balancing a solid green clay block labeled 'Net Profit' on the other side. Clean financial infographics, handcrafted plasticine clay textures, bright elegant studio lighting, tilt-shift miniature perspective --ar 16:9 --v 6.1",

    # 58. (4:04) Setiap kali Anda lupa mengembalikan kaset video film favorit Anda di hari Senin malam,
    "Isometric 3D clay diorama of a panicked clay customer in pajamas on Monday night, suddenly looking in horror at an overdue VHS tape sitting on the coffee table, clock showing 11:55 PM. Handcrafted claymation, expressive comic horror face, warm living room lamp lighting, tilt-shift miniature view --ar 16:9 --v 6.1",

    # 59. (4:10) kasir blockbuster akan menyambut Anda dengan senyuman dingin dan denda 40 dolar.
    "Isometric 3D cutaway diorama at a retro video rental store checkout counter: a stylized clay store clerk handing an extra-long printed paper receipt across the counter to an astonished clay customer holding a video tape. Handcrafted claymation aesthetic, expressive plasticine character sculpting, warm store interior lighting, tilt-shift miniature view --ar 16:9 --v 6.1",

    # 60. (4:16) Pelanggan membencinya.
    "Isometric 3D clay diorama outside a retro suburban storefront at twilight: miniature clay shoppers with disappointed, pensive postures walking to their cars under glowing parking lot lamps, holding long paper receipts. Stylized claymation figures, gentle suburban twilight atmosphere, soft streetlamp lighting, tilt-shift miniature perspective --ar 16:9 --v 6.1",

    # 61. (4:18) Ada rasa bersalah, malu, dan kesal setiap kali melangkah ke meja kasir.
    "Isometric 3D clay close-up at the checkout desk: a dejected clay customer with shoulders slumped and head down in humiliation and guilt, timidly sliding an overdue video tape across the counter to a stern clerk. Handcrafted plasticine, emotive character storytelling, soft overhead counter light, tilt-shift depth of field --ar 16:9 --v 6.1",

    # 62. (4:24) Namun bagi dewan direksi blockbuster,
    "Isometric 3D cutaway diorama of the private Blockbuster boardroom: elite board members in black tuxedos laughing heartily and clinking crystal champagne glasses over a golden tray heaped with late fee penalty cash. Handcrafted claymation, opulent mahogany and velvet decor, warm celebratory chandelier glow --ar 16:9 --v 6.1",

    # 63. (4:27) denda ini adalah sapi perah paling gurih dalam sejarah retail.
    "Isometric 3D metaphorical clay diorama: a literal golden dairy cow made of sculpted clay with dollar signs on its hide, being happily milked by corporate executives into silver buckets overflowing with cash. Handcrafted plasticine, satirical retail humor, bright theatrical stage lighting, tilt-shift miniature render --ar 16:9 --v 6.1",

    # 64. (4:31) Dan disinilah letak jebakan mautnya.
    "Isometric 3D clay diorama inside a retail aisle: an innocent-looking red carpet pathway disguised over a giant mechanical bear trap labeled 'Fatal Trap: Late Fee Addiction'. Handcrafted plasticine textures, warning hazard aesthetic, dramatic suspended suspense lighting, tilt-shift depth of field --ar 16:9 --v 6.1",

    # 65. (4:34) Ketika profit terbesar sebuah perusahaan lahir dari rasa frustrasi pelanggannya sendiri,
    "Isometric 3D conceptual clay diorama: an ominous bubbling vat where dark customer frustration fumes and angry tears are distilled through copper pipes into pure golden coins pouring into corporate coffers. Handcrafted claymation, sinister steampunk satire, vibrant colored vapors, tilt-shift perspective --ar 16:9 --v 6.1",

    # 66. (4:40) perusahaan tersebut sebenarnya sedang berdiri di atas bom waktu yang menunggu pemantik.
    "Isometric 3D clay diorama of a magnificent multi-story Blockbuster corporate skyscraper balancing precariously atop a giant classic cartoon round black bomb with a sputtering, glowing lit fuse, waiting for a single spark to detonate. Handcrafted plasticine clay, intense dramatic tension, high-contrast rim lighting, tilt-shift miniature render --ar 16:9 --v 6.1"
]

target_file = r"d:\projects\YT-Faceless-Automation\prompts_isometric_claymation.txt"
content = "\n\n".join(f"{i+1}. {p}" for i, p in enumerate(prompts)) + "\n"

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated {len(prompts)} prompts into {target_file}")
