import { TestBed, async, inject } from '@angular/core/testing';

import { NoGuardGuard } from './no-guard.guard';

describe('NoGuardGuard', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [NoGuardGuard]
    });
  });

  it('should ...', inject([NoGuardGuard], (guard: NoGuardGuard) => {
    expect(guard).toBeTruthy();
  }));
});
