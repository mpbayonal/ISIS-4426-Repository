import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router'
import { DiseñoService } from 'src/app/servicios/diseño/diseño.service';

@Component({
  selector: 'app-agregar-diseno',
  templateUrl: './agregar-diseno.component.html',
  styleUrls: ['./agregar-diseno.component.css']
})
export class AgregarDisenoComponent implements OnInit {

  constructor(private disenoService: DiseñoService, private router: Router, private activated: ActivatedRoute) { }

  diseno = {
    nombre: '',
    apellido: '',
    email: '',
    estado: false,
    fecha: new Date(),
    pago: '',
    proyecto: this.activated.snapshot.params.idProyecto
  }

  selectedFile: File = null;
  agregarDiseno() {
    const fd = new FormData();
    fd.append('image', this.selectedFile, this.selectedFile.name);
    fd.append('nombre', this.diseno.nombre);
    fd.append('apellido', this.diseno.apellido);
    fd.append('email', this.diseno.email);
    fd.append('estado', this.diseno.estado ? 'Disponible' : 'No Procesado');
    fd.append('fecha', this.diseno.fecha.toDateString());
    fd.append('pago', this.diseno.pago);
    fd.append('location', this.diseno.proyecto);
    this.disenoService.createDiseno(fd).subscribe(
      res => {
        this.router.navigate(['empresa/proyectos/' + this.activated.snapshot.params.idProyecto + '/disenos'])
      }, err => console.log(err)
    )
  }
  cargarImagen(event) {
    this.selectedFile = <File>event.target.files[0];
  }

  ngOnInit() {
  }

}
