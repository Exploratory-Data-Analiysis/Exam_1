# Análisis Exploratorio de Datos: Erupciones solares
Este repositorio contiene 3 archivos:
1. Base de datos (.csv) que contine un total de xxxxx filas y xx columnas.
2. Archivo .py con el programa utilizado para analizar la base de datos.
3. Archivo .pdf que contiene el análisis detallado de la base de datos.

Se tiene una base de datos que contiene información sobre 116.143 eventos de erupciones solares registrados entre *Febrero de 2002* y *Marzo de 2018* distribuida en 18 columnas, a continuación se explica de forma breve el contenido de cada columna.

## Columnas

- **flare:** Número que indifica la erupción solar.
- **start.date:** Fecha de inicio de la erucpión.
- **start.time:** Hora de inicio.
- **peak:** Hora a la que se presenta el máximo.
- **end:** Hora de finalización
- **duration.s:** Duración de la erupción.
- **peak.c/s:** Recuento de picos por segundo	
- **total.counts:** Recuento total de picos 
- **energy.kev:** Energía producida por la fulguración (KeV)
- **x.pos.asec:** La posición X por segundo de arco
- **y.pos.asec:** La posición Y por segundo de arco
- **radial:** Unidad em segundo de arco
- **active.region.ar:** Región activa del Sol 
- **flag.1:** Código de bandera de la fulguración 1
- **flag.2:** Código de bandera de la fulguración 2	
- **flag.3:** Código de bandera de la fulguración 3	
- **flag.4:** Código de bandera de la fulguración 4	
- **flag.5:** Código de bandera de la fulguración 5

## Importante:
 
- Note that only events with non-zero position and energy range not equal to 3-6 keV are confirmed as solar sources.
- Events which have no position and show up mostly in the front detectors, but were not able to be imaged are flagged as "PS".
- Events which do not have valid position are only confirmed to be non-solar if the NS flag is set.
- Peak Rate:  peak counts/second in energy range 6-12 keV, averaged over active collimators, including background.
- Total Counts:  counts in energy range 6-12 keV integrated over duration of flare summed over all subcollimators, including background.
- Energy:  the highest energy band in which the flare was observed.
- Radial Distance:  distance from Sun center
- Quality Codes: Qn, where n is the total number of data gap, SAA, particle, eclipse or decimation flags set for event.
- n ranges from 0 to 11.  Use care when analyzing the data when the quality is not zero.

## Flare flag codes:

- **a0:** In attenuator state 0 (None) sometime during flare
- **a1:** In attenuator state 1 (Thin) sometime during flare
- **a2:** In attenuator state 2 (Thick) sometime during flare
- **a3:** In attenuator state 3 (Both) sometime during flare
- **An:** Attenuator state (0=None, 1=Thin, 2=Thick, 3=Both) at peak of flare
- **DF:** Front segment counts were decimated sometime during flare
- **DR:** Rear segment counts were decimated sometime during flare
- **ED:** Spacecraft eclipse (night) sometime during flare
- **EE:** Flare ended in spacecraft eclipse (night)
- **ES:** Flare started in spacecraft eclipse (night)
- **GD:** Data gap during flare
- **GE:** Flare ended in data gap
- **GS:** Flare started in data gap
- **NS:** Non-solar event
- **PE:** Particle event: Particles are present
- **PS:** Possible Solar Flare; in front detectors, but no position
- **Pn:** Position Quality: P0 = Position is NOT valid, P1 = Position is valid
- **Qn:** Data Quality: Q0 = Highest Quality, Q11 = Lowest Quality
- **SD:** Spacecraft was in SAA sometime during flare
- **SE:** Flare ended when spacecraft was in SAA
- **SS:** Flare started when spacecraft was in SAA

El objetivo de realizar un análisis exploratorio de datos sobre una base de datos de este tipo es observar si las fulguraciones obedecen algún comportamiento estadístico partícular, además de predecir comportamientos específicos como los picos de emisión o las regiones de mayor de actividad de las fulguraciones. 
