import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EditarProyectosComponent } from './editar-proyectos.component';

describe('EditarProyectosComponent', () => {
  let component: EditarProyectosComponent;
  let fixture: ComponentFixture<EditarProyectosComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EditarProyectosComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EditarProyectosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
