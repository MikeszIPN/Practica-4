%Categoria_de_cita
cita('R', 1). %Respiratoria
cita('TA', 2). %Transtornos_alimenticios
cita('M', 3). %Malestar_general

%Preguntas por categoria
preguntas(1,'antecedentes_familiares').
preguntas(1,'tabaco').
preguntas(1,'contextura').

preguntas(2, 'alcohol').
preguntas(2, 'indigestion').
preguntas(2, 'alimentacion').

preguntas(3, 'fiebre').
preguntas(3, 'nauseas').
preguntas(3, 'dolor corporal').

%Respiratorias
antecedentes_familiares('nunca',1).
antecedentes_familiares('a veces',2).
antecedentes_familiares('siempre',3).

tabaco('nada',1).
tabaco('poco',2).
tabaco('mucho',3).
tabaco('excesivo',4).

contextura('obeso',1).
contextura('normal',2).
contextura('delgado',3).

%TA
alcohol('nada',0).
alcohol('poco',1).
alcohol('mucho',2).
alcohol('excesivo',3).

indigestion('nunca',0).
indigestion('una vez',1).
indigestion('muchas veces',2).
indigestion('siempre',3).

alimentacion('vegetales',1).
alimentacion('frutas',2).
alimentacion('pescados y encurtidos',3).

%Malestar
fiebre('nada',0).
fiebre('leve',1).
fiebre('media',2).
fiebre('elevada',3).

nauseas('no',1).
nauseas('si',2).

dolorC('no',1).
dolorC('cabeza',2).
dolorC('brazos y piernas',3).
dolorC('pecho',4).


%Enfermedad
enfermedad(1211, 'Bronquitis').
enfermedad(1123, 'Tos').
enfermedad(1302, 'Asma').

enfermedad(2033, 'Bulimia').
enfermedad(2211, 'Anorexia').
enfermedad(2303, 'Cirrosis').

enfermedad(3311, 'Gripa').
enfermedad(3323, 'Dolor estomacal').
enfermedad(3414, 'Lesion').

%Tratamiento
tratamiento('Bronquitis', 'beber liquidos en abundancia.').
tratamiento('Tos', 'Toma abundantes liquidos, sobre todo tibios.').
tratamiento('Asma', 'Medicamentos de accion rapida.').

tratamiento('Bulimia', 'Terapia con un especialista calificado').
tratamiento('Anorexia', 'Amor propio.').
tratamiento('Cirrosis', 'Antidepresivos, que te anexen.').

tratamiento('Gripa', 'Paracetamol.').
tratamiento('Dolor estomacal', 'Pepto Bismol.').
tratamiento('Lesion', 'Curita :).').


diagnostico(X, Y, Z):- enfermedad(X, Y) , tratamiento(Y, Z).


%write(escribe_) , read(X) , diagnostico(X,Y,Z).