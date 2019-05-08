import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FormOcrComponent } from './form-ocr.component';

describe('FormOcrComponent', () => {
  let component: FormOcrComponent;
  let fixture: ComponentFixture<FormOcrComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FormOcrComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FormOcrComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
