    label prologo3:

        scene kitchen
        ####open_eyes#######dissolve_scene_full########wipeleft###wipeleft_scene
        "Después de una noche de descanso me levanto temprano el día de hoy."
        "Por ahora,  creo que me dispondré de hacer el desayuno para el club del desayuno que hicimos con Sayori, mientras preparo la comida."
        "Me doy cuenta que ya es tarde así cocino lo mas fácil de cocinar con pan, voy por mi uniforme para irme lo mas rápido hacia la escuela."
        scene club_day
        with dissolve 
        ""
        "El día de clases terminó exageradamente rápido, como siempre."
        "Lo bueno al menos no puedo quedarme en casa aburrido estos son los momentos en que le agradezco a Sayori que me incluya en sus grupos."
        "Normalmente nadie se da cuenta que ¡Es un club de 4 lindas chicas! aunque solo estoy yo."
        "Por ahora tengo una mini cocofonia, o algo así."
        "Voy agitando el lapicero mientras... Que tengo una pequeña imaginación."
        "Como si una gran guerra por... ¿Tu mamá?."
        "Pero no es valido responder afirmando algo con un quizas, ya que al afirmar no hay cabo para un quizas."
        "Pasar mucho tiempo con Monika escribiendo poemas me cambió."
        play sound XD1
        "Mientras divago por mi pensamientos escucho unos pasos en el pasadizo. Ya que este lugar es muy olvidado, normalmente nadie le da importancia a un cartel de... ¡Club de literatura!"
        "Pues lo normal es que al ver literatura, parezca aburrido."
        "De hecho yo ni siquiera quería unirme."
        pause 3.0
        "Esos pasos ya me están cansando."
        "¿Es que acaso no tiene algo mejor que hacer?"
        "Me levanto para ver que pasa."
        stop sound
        "Parece que ya paro."
        "Igual salgo de este lugar."
        scene corridor
        with dissolve
        "Salgo y veo a un chico de apariencia generica, aunque solo tiene unos tres mechones de pelo junto a unos ojos grises."
        "Nunca he visto a alguien así por aquí, de hecho al único que he visto fue a (Chad)."
        "Ese tipo, se me queda mirando. ¿Que hace aquí es acaso un baboso?"
        show Ap1
        a "Hey, ¿este es el club de literatura?, Por cierto soy Astora."
        mc "Si pero en este momento no hay nadie solo yo estoy en este lugar"
        a ap1 "Pero... ¿no hay mas integrantes? osea no creo que se pueda hacer ¿Un club de una persona?."
        menu:

            mc "¡Claro!": 

                mc "¿Acaso andas pendejo para saber que se puede hacer un club de una sola persona?"

                $ le dijiste ="no"
                pass

        a "Está bien y si a veces ando medio pendejo, bueno un gusto hermano."
        "Ese tipo se fue caminando."
        "Puff ese tipo se lo ha creído, bueno uno menos."
        "Aún no entiendo por que no se dan cuenta que este es un club de mas de cuatro chicas."
        "Bueno seguiré perdiéndome en mis pensamientos."
        "Regreso al salón."
        scene club_day
        with dissolve
        "Después de esperar un muy buen rato. Sayori entra al salón del club."
        show sayori 1a
        s "Hola..."
        s "[player]. ¿Desde cuando eres el primero en club?"
        mc "Hoy mis clases terminaron antes así que vine al club, aunque ando esperando desde hace un buen tiempo."
        s 5b "Bueno... ¿Me acompañas a comprar algo de comer.?"
        "Inmediatamente ya se lo que me está pidiendo pero aun así cedo."
        s 4bs "¡Gracias!"
        #Cambia scena a Monika
        scene piano 
        with open_eyes
        m "No se que hora es."
        m "Estoy desde hace un buen tiempo tocando la pieza que compuse."
        menu:

            "Perderte en el tiempo" :

                
                $ lo sabes ="no"

                pass
                
            
            "Continuar con la pieza" :


                $ lo sabes ="si"
                
                call pieza

                pass

        scene club_day
        with dissolve
        s "Parece que Monika se perdió tocando el piano."
        mc "Pues teniendo en cuenta que toca muy bien creo que valdrá la pena esperar."
        mc "Quien sabe si está practicando para tocar frente a nosotros, ¿recuerdas el día en que lo dijo?."
        s "Y si... ¿Está pensando dejar el club?."
        mc "Lo dudo rotundamente."
        "Mientras hablo, la puerta se abre y pasa Natsuki junto a Yuri."
        y "H-hola..."
        s "Holi... Yuri."
        "Sayori se va a charlar con Yuri."
        "Yo mientras tanto observo a Natsuki ir por su colección de mangas."
        "Bueno voy hacia ella para conversar de algo."
        show natsuki 2b
        n "Oye! tu [player] compre un manga nuevo."
        "Yo sin saber de que se trata voy hacia ella fin al cabo no tengo nada que hacer."
        "Voy hacia ella."
        mc "Hola Natsuki..."
        n "¡Hola tonto!."
        "Ahora ella está insultando, me pierdo en mis pensamientos."
        "En el momento que estaba ella sacaba su manga, Monika sale de la puerta."
        m "¡Hola!."
        show monika 1l
        show at left natsuki 1bb
        n "¿Donde has estado! Por qué has tardado tanto tiempo."
        m "Me pasé un poco con el tiempo. Pero tengo una buena noticia..."
        m 4b "Conseguí un nuevo miembro."
        n 42be "¿Y Donde esta ese nuevo miembro?."
        "Para este momento veo a Monika un poco preocupada."
        m h1_4l "El ha dicho que prefiere asistir mañana de tal manera que traerá un poema."
        n "No parece tan convincente esa unión."
        s "Y... Si tal vez solo... ¿Quiere quedar bien?."
        y "Suena a-a una bonita forma de decir que no."
        n "Nadie aquí seria lo suficiente cuerdo coma para unirse a un club en que hay solo cuatro chicas y un chico."
        m "Eso es bastante valido, es por eso que lo invité al club."
        m "Ya qué, ni siquiera sé que hace aquí. O al menos por que vino."
        n "Wow, que gran excusa para eso alch."
        s "Pero, ¡por qué esa actitud!."
        show monika 2i
        m "Bueno tengo esperanzas que el si venga al club para mañana, pero ahora. ¿Qué les gustaria hacer?."
        n "¿Ya qué?"
        "Vaya atmosfera que da Natsuki ahora."
        "Me pregunto... Que habrá pensado ella cuando viné aquí, sea lo que sea."
        "Saber que un nuevo... Amigo vendrá aquí para participar con nosotros en la mayoria de reuniones."        
        "Dejo de pensar en ello."
        "Mientras veo a todos estar muy divertidos converzando yo... Como de costumbre estoy solamente mirando la habitación."
        "Es realmente extraño saber que un nuevo miembre vendrá, ¿será algún tipo raro?."
        s "No te preocupes, no por que un nuevo miembro vendrá quedaras en segundo plano."
        mc "Esa no la mayor de mi preocupación."
        mc "Es mas..."
        "Bueno, sí. Es la mayor parte de mi preocupación."
        s "Jeje, Es un poco lindo verte celoso por solamente un nuevo miembro."
        mc "Ahh jajaja, por ahora eso no tiene reelvancia."
        s "Así que ¿Terminamos la reunión y vamos a caminar con alguíen mas?"
        mc "Suena a una buena idea, así que queda."
        mc "Así que creo que en breve comenzará la actividad del club, ¿Te parece si planificamos lo de salir mas tarde?"
        s "De acuerdo."
        n "A ver Monika... Dejame entender, ¿Un nuevo papanatas vendrá solo por que lo encontraste tocando un piano?"
        m "Jeje, sí "
        



    label pieza:

        scene piano 
        with open_eyes
        #bueno seria buena idea ponerle una clase de animación o en la parte superior poner algo como "Estas jugando como Monika!"
        play music mpiece
        m "Desde que todo del festival fue cancelado he tenido mucho tiempo para poder practicar."
        m "Es parte del alba lo cual me permite mover los dedos, decia cierto poema."
        m "¡Ahora me sale mucho mejor!"
        "Es la musica lo que permitirá que pueda expresar. Es algo emocional, tocar el piano es magico."
        "Ni siquiera se que hora es. En menos de lo que me doy cuenta he perdido la noción del tiempo."
        "Solo sigo tocando."
        play sound closet_open
        "Escucho que la puerta se abre... Creo que es Natsuki recordándome de la existencia del club."
        "Normalmente la que suele entrar así es Natsuki exigiendome ir al club."
        "Así que responderé lo de siempre"
        m "¡Dejame terminar esta pieza por favor!."
        "???" "Esta bien..."
        "Espera esa voz no es de Natsuki."
        "Y tampoco es [player]."
        "¿Por qué esta aquí?, tendré que preguntarle ahora de quíen será."
        m "Disculpa, ¿quien eres?"
        a "¡Hola Soy Astora!, solo un tipo que solo llego aquí de casualidad."
        m "¿Astora?..."
        "Eso nunca he escuchado alguna vez en dentro de esta escuela."
        "Pero mis pensamientos se pierden mientras toco."
        "Bueno seguiré tocando, mientras con el rabillo de mi ojo veo a ese tipo buscando un asiento."
        "Parece que es del colegio. Lo sé porque tiene el uniforme."
        a "¿Te importa si me quedo a escuchar?."
        "Mi amabilidad me obliga a responder si."
        m "Si."
        "El pone su silla en un lugar un poco separado de donde estoy tocando de tal manera que le deja escuchar y ver como toco."
        pause 6.0
        a "Espera... Eso es ¡Your Reality!."
        m "Sí..."
        "Eso me pone un poco extraña ya que solo las chicas y [win_user] saben eso."
        "Esto se esta poniendo raro."
        "Ahora si que volteo a ver a ese tipo."
        stop music
        show Astora  Ap11
        play song ma1
        "Lo veo a la cara y..."
        a Ap13 "Yo te conozco... Eres... Bueno solo se que te vi en ese salón del club de literatura... Pero No se tu nombre."
        m "Bueno un gusto soy Monika líder del club de literatura."
        a Ap3 "¿Que no el club de literatura es de un solo miembro?."
        "Suelto una pequeña carcajada"
        m "Claro que no de, echo somos como cinco personas. Somos Cuatro chicas y un chico..."
        a Ap11 "Huy!. Y... ¿Como son los demás miembros?."
        "Para este momento recuerdo que es el tipo que vino del supuesto departamento de clubs. Y que también es muy parecido a [player] solo que mucho mas despeinado y con ojos grises."
        m "Primero esta Sayori. Una chica que normalmente es muy activa y feliz normalmente ella anda alegrando el día al club."
        a "Wow entonces debe ser una buena líder..."
        m "Si de echo ella es vicepresidenta, Ella es capaz de terminar una pelea."
        a "Eso parece... ¡Genial!."
        m "Luego viene Natsuki. Ella es una pelirosa un carácter algo rudo y que le gusta el manga, de echo ella suele decir que es literatura."
        a "Pero asta cierto punto es literatura asiática."
        m "Es un poco divertido por que tiene su colección de mangas en el closet del club."
        a ap2 "Eso puede llegar a ser divertido."
        m "Y por último pero no menos importante esta Yuri ella es la chica más madura del grupo... Ella normalmente esta leyendo libros de horror o suspenso."
        a "Parece muy placentero estar en tu club."
        m "Sí..."
        "Doy una pequeña sonrisa."
        m "Casi olvido a [player]. El es muy amigo de Sayori, es un chico normal que se dedica a leer manga y otras cosas."
        a Ap13 "¿Y solo cinco?..."
        m "Si somos cinco por que no a muchos les interesa la literatura."
        m "A veces pienso que Sayori se unió por que le pareció divertido comenzar un club."
        a Ap2 "Y con literatura te refieres a leer libros o cosas como analizarlos o escribir poemas incluso... ¡Recitarlos!."
        m "Algo así. de echo te ¿gusta la literatura?."
        a "Bueno me gusta leer libros y de vez en cuando escribo poemas solo por diversión."
        "Bueno me gana la curiosidad de saber de donde vino."
        "Se me ocurre invitarlo."
        m "Bueno estamos en busca de nuevos miembros para el club... ¿Quisieras unirte?"
        a "¡Pues claro que si! ¿cuando no empezamos?."
        m "En este momento te llevo al club."
        "No entendí muy bien lo que quiso decir."
        a As4 "Hee...¿Puedo venir mañana?."
        a As5 "No lo tomes a mal, es que quiero inspirarme para escribir un poema para presentarme en especial con gente tan experimentada, me refiero que me presento y luego recito. "
        a "Aparte que al escucharte tocar el piano quería esperar a que terminaras para tocar un rato. JEJE."
        m "Sabes tocar el piano?."
        a Ap3 "Emm si de manera decente, de echo ¿Puedo tocar?."
        m "Claro."
        "En este momento me hago a un lado sentándome en la silla que el trajo solo para que el se ponga a tocar."
        a "Y... ¿Que te inspiro a crear el club?"
        m "Mi pasión por lo que es recitar y analizar lo que hay detrás de esas rimas de palabras."
        m "Incluso un lugar donde pueda divertirme y divertir a otros con los poemas."
        stop music
        a Ap11 "Parece que te dedicas demasiado a tu club."
        a Ap13 "Y.. No es por querer votarte o nada, pero como líder no deberías estar en tu club?"
        m "Hmm no creo ya que si les traigo un nuevo miembro valdrá la pena."
        a "Bueno yo iré mañana he he para traer de paso un poema."
        m "Vale yo iré hacia el club de paso para comentarles tu unión"
        "Procedo a irme por la puerta. el saca unas partituras como si estuviera listo para tocar."
        play sound closet_close
        return

    label say:
        
        c"no se que te paso"
        "empiezo a hablarle sobre todo lo que recuerdo"
        if prometiste =="no":
            c"pero Monika estaba un poco mas sentimental después del la reunión del club"
            "↕? 4☻6☻3☻121I§21☻1☻1☻1☻1§§2☺6☺6☺6♦♥♦3"
            "Z2>6☻1♥1S2♥4♥1☺â242"
            "yo..."
        
        
        if prometiste =="si":
            "realmente me siento mucho mas emocionado de lo normal"
            "Gracias a que estoy mucho mejor por visitar a Sayori"
            "todo está mucho mejor"
        
        
        
        "procedo a contarle lo sucedido a Sayori"
        return
        
        
    
   