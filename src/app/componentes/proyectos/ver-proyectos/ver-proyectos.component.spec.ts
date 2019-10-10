import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { VerProyectosComponent } from './ver-proyectos.component';

describe('VerProyectosComponent', () => {
  let component: VerProyectosComponent;
  let fixture: ComponentFixture<VerProyectosComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VerProyectosComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VerProyectosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
