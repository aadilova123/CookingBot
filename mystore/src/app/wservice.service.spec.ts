import { TestBed } from '@angular/core/testing';

import { WServiceService } from './wservice.service';

describe('WServiceService', () => {
  let service: WServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(WServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
