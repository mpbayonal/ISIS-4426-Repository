import { Component, OnInit } from '@angular/core';
import {Router, ActivatedRoute} from '@angular/router'
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
    urlArchivo: null,
    proyecto: this.activated.snapshot.params.idProyecto
  }

  selectedFile : File= null;
  agregarDiseno(){
    const fd= new FormData();
    fd.append('image', this.selectedFile, this.selectedFile.name)
    this.diseno.urlArchivo= fd;
    this.disenoService.createDiseno(this.diseno).subscribe(
      res=>{
        this.router.navigate(["empresa/proyectos/"+this.activated.snapshot.params.idProyecto+"/disenos"])
      }, err => console.log(err)
    )
  }
  cargarImagen(event){
    this.selectedFile= <File> event.target.files[0];
  }

  ngOnInit() {
  }

}
