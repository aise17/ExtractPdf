import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MarcoFormOcrComponent } from './marco-form-ocr.component';

describe('MarcoFormOcrComponent', () => {
  let component: MarcoFormOcrComponent;
  let fixture: ComponentFixture<MarcoFormOcrComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MarcoFormOcrComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MarcoFormOcrComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
