import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarDisenosComponent } from './listar-disenos.component';

describe('ListarDisenosComponent', () => {
  let component: ListarDisenosComponent;
  let fixture: ComponentFixture<ListarDisenosComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListarDisenosComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListarDisenosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
