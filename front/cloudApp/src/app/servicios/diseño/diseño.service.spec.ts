import { TestBed } from '@angular/core/testing';

import { DiseñoService } from './diseño.service';

describe('DiseñoService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: DiseñoService = TestBed.get(DiseñoService);
    expect(service).toBeTruthy();
  });
});
