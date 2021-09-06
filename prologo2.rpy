    label pd:
        
        scene bg parknigh
        with fade 
        
        "Despierto en el mirador sin saber como o porque."
        mc"¿Pero como llegue aquí?"
        "Me paro y hago presencia sobre lo que veo en este mirador."
        "No encuentro la manera de salir, solo un camino hacia el bosque."
        "Lo analizo, parece ser el camino, empiezo a caminar, perfecto parece que estoy perdido."
        
        mc"Oh, tal ves no."
        "Menciono en voz alta, a lo que sin rumbo me paso caminando para encontrar la ciudad."
        "Tengo varios pensamientos sobre que debo hacer, pero ya he decidido, no creo poder volver ahora."
        "Ya no tengo noción del tiempo, ¿que día es? ¿Que hora es?, no lo se."
        if prometiste =="si":
            call positivo from prologo1_rpy
            pass
        scene l1 
        with fade
        "Pasaron horas y horas, y aun no logro encontrar el camino."
        "Se siente como una eternidad en lo que camino."
        mc"¡Ah, necesito salir!"
        "Por alguna razón, lo grite." 
        scene l3
        "Después de una larga caminata, logro darme cuenta que ni siquiera estoy en mi ciudad, ¿Y como demonios llegue aquí?"
        mc"Sigo caminando sin rumbo, con esperanzas de encontrar un lugar donde pasar la noche."
        "Después de un rato, logro encontrar un hotel."
        e"Perfecto, tenemos un cuarto para usted."
        "Reviso mi billetera en busca de dinero."
        "Saco la cantidad de dinero suficiente, parece que si tenia cambio."
        scene l2
        with fade 
        "Logro acomodarme, mientras pienso como demonios pare aquí." 
        "Tengo que irme mañana, tengo que lograr ubicarme en el tiempo."
        "Ni siquiera, se que día es."
        
        #ocupar un video de cambio de dia
        
        "Despierto algo cansado, pero estoy bien, pudo ser peor."
        "Me alegro de que no paso nada, uff"
        scene l4
        with fade 
        mc"Después de un momento, logro tener una ubicación de donde podría estar, ahora necesitare salir."
        "Busco y que busco, y logro encontrar una terminal de viajes."
        "Primero, tengo que buscar un bus."
        "De preferencia que no tenga muchos pasajeros."
        "Enfermarme de alguna gripe o virus no seria lo ideal."
        scene l5
        with fade 
        "Bueno, tengo dinero suficiente para irme de aquí."
        "Después de comprar el boleto."
        "Me pregunto, ¿Que paso con las chicas? ¿Que paso con ellas?"
        "Después de un tiempo logro entrar a un bus, pero aun no estoy ubicado del todo."
        "¡Y ni siquiera se como llegue allí!."
        "Bueno, no importa, ahora ya estoy de camino a casa, parece que logro ubicarme de que es un sábado. Creo que esta bien..."
        "Perfecto, ahora... ¿¡Que sucedió el viernes!?, solo se que estaba con mi uniforme."
        "Recién me doy cuenta que estoy con mi uniforme ahora que me veo, ¡¡¡¡pero que demonios!!"
        "Hmmmm"
        #parar la musica antes de esta ecena porfas no olvidar 
        scene t1
        with fade
        "De camino a casa, tengo la alegría de recordar que estuve con Monika una vez cuando fuimos de paseo."
        "Estuvo genial."
        "Bueno, después de tener varios pensamientos en el viaje, parece que ya estamos llegando."
        "Fue muy agradable el viaje, aunque fue sin motivo."
        "Después de un momento, logre llegar a mi ciudad."
        #ejecutar una musica del ddlc
        scene t2
        with fade 
        "Despues de un tiempo, bajo del tren."
        "Ahora, estiro las piernas y doy un bostezo."
        "Listo para ir a casa, si, eso fue duro pero se como volver."
        scene pf
        with fade
        "Necesito hablar con Sayori, no... mejor la visitare."
        "Hmmm, visitar a Sayori? Eso estaría genial hace días que no lo hago, aunque si que me hablo muy constantemente con ella."
        "Es bueno verla, tan brillante y tan energética."
        "Siempre encuentra la manera de hacer a todo genial, hehehe."
        "Bueno, ya estoy llegando a casa."
        scene pg
        with fade
        play music t2
        "Recordar la gran caminata del terminal de viajes a casa es muy des estresante, llego de la manera mas cariñosa a mi casa."
        scene ph
        "Abro gentilmente la puerta de mi casa con un gran grito. "
        mc"¡¡¡Porfin, mi casita!!!"
        "Entro en mi cuarto y.... nada."
        scene bedroomn 
        with fade 
        "Solo quiero descansar, ahora si que estoy exhausto."
        "Me alisto para dormir, ya parece ser de noche."  
        "Me echo en mi cama, pensando en como la pase para llegar aquí."
        "No se como llegue allí, tengo muchas preguntas."
        "Cierro mis ojos y por fin, me duermo."
        stop music
        #pasar video de trancicion para mas emocion en este momento
        scene kitchen
        with fade
        "Mi cabeza se nubla por todos los pensamientos de ayer, pero no le doy la debida importancia."
        play music t2
        "Pero preferiré hacer algo para comer."
        "Saco unos cupcake que me regalo Nat hace unos días."
        "Junto a una jalea de piña, los panes de canela toman un delicioso sabor."
        "Lo crujiente del pan con lo caliente que esta es tan delicioso."
        "Mi casa esta algo sucia."
        #insertar musica de cocina 
        scene mclivingday
        with fade
        "Mientras ordeno un poco mi sala, me pongo a pensar: Y si mis padres viniesen ¿Que dirían?"
        "Me digo a mi mismo, discutir con mis padres seria como luchar contra ornstein y smough."
        "De ser así estaría fregado, no solo eso, no tengo la manera de ganar serian como el duo inseparable."
        "Recuerdo esos momentos que jugué con Monika y Soleire, me ayudaron en ese combate."
        "Fue muy divertido."
        stop music
        "Cuando Sayori cocino en mi cumpleaños, y termine por comer pollo crudo."
        "¡Ah trauma de Vietnam!"
        "Desde ese día algo cambio dentro de [player]."
        "Mi gusto por el pollo se quebró."
        "Por fin me dedico a salir de mi casa para ir a visitar a Sayori, al fin veré, ¿Que paso el viernes?"
        scene he
        with fade
        #Nota conseguir sprites de las dokis casuales
        s" ¡¡¡¡Hey hola!!!!"
        mc"Uh, hola, que gusto verte, ¿Como has estado?"
        s"Como has estado."
        "Tengo la sensación que ella empieza a temblar de manera frenética y empieza hablar tartamudeando."
        s"¿Te-ee gustari--a p pa-sar?"
        "No logro entender como llegamos a esto, pero asiento."
        "Paso a su casa, ella empieza a moverse con gran torpeza."
        scene hc
        with fade
        "En menos que me de cuenta estoy su cocina."
        "Terminamos conversando por cosas del pasado, fue muy divertido."
        "Hablando de todos los intentos de hacer un gran poema."
        scene seh
        with fade 
        "Con alegría le pregunto que sucedió el viernes."
        s"Lo de siempre, compartimos poemas y te fuiste si tan siquiera esperarme."
        s"Aunque Monika intento hablarte pero decidiste no hablar."
        "No se realmente si tendremos algo sobre el festival?"
        "Decido preguntar que sucedió, y si que tenemos algún trabajo incluso que sucedió con el festival."
        s"Mas bien, ¿tu que hiciste el viernes?"
        "De alguna manera, me siento apuñalado o marginado."
        mc"Pues... Yo..."
        "No se como responder a la pregunta, ¿Que debo eligir?"
        menu:
            
            "Pues nada en especial, lo de siempre.":
                
                c"¿Enserio? Me pudiste haber llamado para poder ver una película."
                $ mentiste ="si"
                pass
            
                 
                 
            
            "No se que paso, solo me aparecí alli":
                
                c"Que!!?"
                $ mentiste ="no" 
                call say
                
                
             
        s "Bueno... El festival fue cancelado dos días antes de que te volviera a ver."
        s "Y no estábamos preocupados del festival, se dice que sera en unos meses."
        mc "Woah, eso esta mucho mejor."
        "Podría jurar que el viernes estábamos planificándolo todo para el festival."
        "Como dije, no tengo la menor idea, creo que incluso le ayudare a Yuri hoy que es domingo, hehehe."
        #insertar video de glich
        "No tengo idea de lo que ha sucedido, abrazo a Sayori, pero no logro reconocer su cara, ni su cuerpo, lo que logro ver de su cara es un montículo de carne negra como si hubiera sido quemada..."
        "¿Que carajos?"
        show sombra
        "No tengo idea de que demonios esta pasando, no puedo seguir con esto, es como si un olor se disolviera, como si fuera amoniaco."
        "No puedo seguir, cierro los ojos tratando de entender que sucede"
        show blacksayori
        with fade 
        "Ahora la sombra es reconocible pero... ¿Que sucede?"
        "No puedo mas..."
        
        
        with fade
        scene bedroom
        with fade
        
        #inserte musica de silent hill
        #inserte imagen del lugar
        play music bm1
        "He despertado en una parte aleatoria del salón del club."
        "Llego a la concluir que estoy en algún tipo de reunión."
        "Después de pensar un rato... "
        
        
        scene  ns
        with fade 
        
        #parte la musica de silent hill no parara"
        #hollow music inserte a qui en vez de silent hill ,para mas tarde
        "Pero no tengo la mas mínima idea de como demonios llegue hasta acá..."
        menu:
            
            
            "Debería..."
            
            
            "Buscar en el club":
                
                "Pasan horas... Creo que estoy en el otro local de la escuela."
                $ trataste ="no"
                
                
            
            
            "Tratar de orientarme":
                
                "Me di con la sorpresa de que estoy en el otro local de la escuela." 

                $ trataste ="si"
        
        stop music
        scene seh
        with dissolve
        "Suspiro. Estoy sudando se siente como si mi cuerpo se controla solo."
        "Que mal sueño..."
        "Ahora en casa, me siento mucho mas seguro..."
        play music bm0
        "Ya no tengo mas preocupaciones, ya todo terminó. Para este instante estoy acostado en mi cama."
        "Miro mi ordenador, nada, pero ahora escribiré un poema, miro con melancolía a la ventana y..."
        "Tengo el lápiz con ganas de escribir pero... tendré la oportunidad."
        "¿Una luz es lo que veo?"
        stop music 
        "Después de intentar recitar este poema."
        "Recuerdo que... ¡¡Tengo que visitar a Sayori!!"
        "Tomo mi ropa casual, recordando que es Domingo y voy directo a su casa."
        scene he
        "Toco su puerta, pero en la otra esquina veo a otra persona ajena a todo este barrio, parece ser ajeno a todo esta situación."
        "Me gustaría estar como el, sin preocupaciones y poder caminar de manera tranquila pero..."
        "Ella me abre la puerta de manera alegre."
         #Este... Necesito el nombre de los sprites pero lo intentare

        play song t8
        show sayori 4bc
        s "Oh, hola [player], que alegría tenerte aquí."
        mc "Bueno, realmente no se que paso el viernes."
        "Para este instante, no se me ocurre nada mejor para decir."
        #Chale...
        s "Bueno, exactamente no recuerdo muy bien."
        s 4bx "¡¡Ya se!!. Cuando te fuiste con un tipo vino a preguntar, por parte de un departamento de seguridad de clubs. Si todo estaba bien."
        s "Y Monika muy extrañada con muchas risas le contesto que no pasaba nada. Ella nunca había sido avisada ni por el código de echo no estaba allí."
        s "Ella sabia exactamente que la persona que se habia aparecido no tenia nada que ver con todo el código del juego."
        s "Después nos pregunto si sabíamos que si conocíamos ya que el no estaba en el código."
        stop music
        mc "¿¡QUE!? ¿¡QUE CODIGO!?"
        #Black necesitare en esta parte que llames a la consola y un texto de diga deshabilitar memoria de Mc = True 
        #y con eso ya estaria supongo 
        s 1bj "Te lo diré a ti de manera exacta, parece que hay alguien en el código, un personaje que no esta en el código, ni en la carpeta." 
        s "Y por como esta Monika parece que ni ella explica lo que sucede."
        s "Bueno, MC parece que, te tendré que borrar la memoria de lo que escuchaste."
        s "Lo siento... no se puede dejar así, hehe."
        s 2bb "Aunque parece que ignoras toda la conversación, después de hacer todo tipo de preguntas..."
        #bueno otra vez la consola y pones el texto de persistent memory = false y no usaremos eso hasta el proximo label
        #En el dia de los inocentes pondras: Borrando memoria del pendejo :V
        play music t8 
        s "Al parecer ya casi el ya-a, no tiene tanto control sobre si mismo, ahora solo ignora todo lo que tiene que ver con el código."
        s 2bn "Ahh, casi lo olvido, ese tipo estaba muy preocupado. Y luego nada, solo te fuiste. No hemos escrito ni recitado poemas."
        "Sayori me da una invitación para pasar a su casa con tal de que la ayude en su tarea, procuraré no tener ningún tipo contra tiempo, solo será un tiempo de calidad con ella."
        scene sayori_bedroom
        with dissolve
        stop music
        "Pedire algo para comer... ¿Que debería pedir?. ¡Ya se!, . Una pizza y para mi que sea una lasaña "
        play music gm3
        "Mientras la ayudo recuerdo los muy buenos tiempos de nuestra niñez, es muy lindo volver a verla tan alegre cuando escribe."
        "Seguimos haciendo su trabajo, la alegría nos invade al ver que ya llegó la comida."
        show sayori 4br 
        #Chompilas JSJSJS
        "Desempacó toda la comida, ella esta muy feliz y por consecuencia yo también... Eso sonó como letras de algún rap."
        mc "Hey... ¿Sayori cuanto calculas que tardaremos en tu tarea?."
        "Se lo digo por que me he antojado de unas partidas del Pubg. Pero me sentiría mal si la dejo así."
        s 3bo "¡Esta muy complicado!... No se como podría hacerlo sola." 
        s 1bl "[player] gracias por estar aquí."
        #Para los inocentes no olvidar la musica por y para nada instrumental para ¡¡¡nada!!!
        "Esas palabras me conmueven y activan mis instintos de hermano mayor."
        "Pasan horas y al fin logramos terminar su tarea y nos damos cuenta que era exactamente la parte que no debía hacer."
        "Suspiro, la acaricio en su hermoso peló coral."
        show sayori 3bq
        pause 0.3
        "Bueno, termino de hacer mis comentarios y de pagar al amable señor, que nos trajo la comida. Yo, por algún tipo de suerte tenia dinero para pagar la comida."
        "Despues de una agradable tarde con, Sayori logramos terminar toda su tarea si que fue una gran odisea, fue una bonita tarde de alegría con mi querido sol."
        stop music
        "Le doy una muy buena despedida."
        #Black toda la parte de la casa de Sayori es un relleno que se me ocurrio bueno solo lo digo por que me parecio interesante decirtelo xd
        scene seh
        with fade
        "Por fin después de este día vuelvo a la presencia de mi cuarto "
        "Miro mi ordenador y el me llama, no creo poder resistir mas quiero... Jugar Pubg no lo puedo evitar es evidente."
        "Procedo a prender mi ordenador y iniciar el juego."
        pause 0.1 
        "Después de unas horas de maravillosas partidas. Por fin me voy a dormir"
        #Black en caso no aparezcan las musicas que pongo no desesperes que en unos Dias mes desocupare y hare las definiciones de sprites y ost bueno no tengo mas comentarios
        "Acurrucado en mi cama pienso, ¿como llegué hasta ese mirador?, ¿Que paso en todo el tiempo que me fui?. Solo necesito dormir por ahora."
        "No puedo dormir. Ya no tengo control con migo..."
        play music clair 
        "Yo no quiero. Hmm este ¿Sayori ya habrá terminado su tarea? seria un buen momento. Ya mañana tendré que ir a clases."
        "Bueno ni siquiera estoy con mi pijama así que es hora de ir. Me pongo mi casaca y... Perfecto es hora de irme."
        "Paso por mi sala y hora de irme."
        play sound "audio.closet_open"
        scene he
        "Bueno ya que me encuentro aquí, encuentro la puerta de la casa de Sayori abierta. ¿Espera yo mismo la deje abierta?."
        "Me doy un golpe a la cabeza por tonto, bueno entrare a su casa sin que ella se de cuenta, de paso que termino de ayudarla."
        scene black
        "Por ahora estoy ya de camino a su cuarto, en el pasillo que esta oscuro. ¿La escucho recitar?."
        "Ya que estamos aquí asomo mi oreja para escuchar aun mejor el poema que esta recitando."
        #Bueno black se quedara sin audio aqui hasta que obtengamos el audio.

        "Wow eso es... Muy poético incluso para ella, asomo mi cabeza para ver que esta haciendo..."
        "Si sigue haciendo tarea. Y parece que no le falta mucho."
        stop music 
        "Ella ya esta muy cansada y yo desde aquí espiando bueno es muy buen momento para irme ."
        "Con cautela camino hacia la salida de su casa."
        scene he 
        "Ya que estamos aquí cerrare la puerta de su casa, no sea que me olvide de nuevo."
        play sound "audio.closet_close"
        #Hey black en el cuadro que tengo se pondrá como notificación  de cambio
        #Osea un texto que diga que cambias de personaje.
        "Bueno ahora creo que me iré a casa, ya no tengo mucho que hacer."
       #Este inserte texto de cambio de personaje 
        scene bg nightsky
        m "Todo parece estar, mal ese tipo ni siquiera parece estar del todo en el código base es una ¿clase de personaje como Alice?, aunque su presencia era mas notable."
        m "De el es casi inexistente la pregunta es. ¿Que quiere hacer en este lugar? por que vino a preguntar de esa manera tan seca tendrá algo."
        m "Seria interesante hablar aun mas con el, seria seguro como se si no es alguien malicioso, mientras mas pienso en el mas curiosidad me da en querer conocer sus intenciones."
        "He estado mirando el cielo mientras hablaba no tengo mucha noción del tiempo. Sigo caminando con dirección a mi casa."
        "Aun recuerdo la despedida de Alice se fue y casi nadie se dio cuenta pero como el entro a este juego sin que ni yo me diera cuenta, de echo ni el código se ve afectado."
        "He estado aquí ya por un buen tiempo, ya paso casi una hora es buen momento para ya llegar a casa."
        scene bg streetnight

        m "Ya estoy desde hace un buen momento caminado, ya estoy llegando a casa."
        m "Todo ha sido muy normal desde que Alice se fue alguna que otra reunión y alguna actividad fuera del club, por el mismo echo de que no necesitamos mas guion para poder hablar. "
        m "Casi como una realidad, aunque aun tenemos algunas limitaciones ya que [player] no puede ver algunas cosas que hacemos."
        m "Es como si después de cada historia solo se cierra cada interacción con, es casi una auto eliminación... Pero ya esta el de nuevo junto a ese tipo."
        m "Ni siquiera me moleste en preguntar su nombre, bueno ya casi estoy llegando. Ya me empieza molestar el echo de no saber de donde viene."
        "Ya en casa, lista para abrir la puerta la brisa de la preocupación choca contra mis pensamientos. "
        m "Tranquila ya no deberían pasar mas cosas que afecten a este mundo, pero... Si el hace algo..."
        pause 0.3
        m "¿Que... pasara con nosotras?."
        m "Recuerdo las grandes historias, mundos y todo por lo que hemos pasado. Bueno ya tengo que entrar."
        m "Antes de entrar hacia mi hogar doy una vista hacia la luna, quisiera que... No fuera la misma de siempre."
        scene black

        menu :

            "deberia...":

               "¿Podría preguntar?" :
                    
                        $ ¿Que harás? ="yo"




            "..." :


                $ ¿Que harás? ="no"
                        
            pass     

        if prometiste =="nada":

            m "Y si ese tipo tiene algo que ver con lo sucedido con Alice."
            m "La ultima vez que vino algo que no tiene que ver con el juego original se bugeo."
            m "El vendrá mañana, en caso que si venga... Seria muy interesante preguntarle algunas cosas."
            pass

        m "Entro a mi casa lista para descansar mañana, ya veré que haremos en la reunión."
        return


        label say:
        
        c"no se que te paso"
        "empiezo a hablarle sobre todo lo que recuerdo"
        if prometiste =="no":
            c"pero Monika estaba un poco mas sentimental despues del la reunion del club"
            "↕? 4☻6☻3☻121I§21☻1☻1☻1☻1§§2☺6☺6☺6♦♥♦3"
            "Z2>6☻1♥1S2♥4♥1☺â242"
            "yo..."
        
        
        if prometiste =="si":
            "realmente me siento mucho mas emocionado de lo normal"
            "Gracias a que estoy mucho mejor por visitar a sayori"
            "todo esta mucho mejor"
        
        
        
        "procedo a contarle lo sucedido a Sayori"
        return    
