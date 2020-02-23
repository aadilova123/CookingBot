import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WSearchComponent } from './w-search.component';

describe('WSearchComponent', () => {
  let component: WSearchComponent;
  let fixture: ComponentFixture<WSearchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WSearchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
