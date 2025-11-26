# runtime settings
hooks = dict(
    type='EvalHook',
    high_keys=[
        'MR-full-mAP', 'MR-full-mIoU', 'HL-min-VeryGood-mAP',
        'MR-full-mAP@0.1', 'MR-full-mAP@0.3', 'MR-full-mAP@0.5',
        'MR-full-R1@0.1', 'MR-full-R1@0.3', 'MR-full-R1@0.5',
        'MR-full-R5@0.1', 'MR-full-R5@0.3', 'MR-full-R5@0.5',
        'MR-full-R10@0.1', 'MR-full-R10@0.3', 'MR-full-R10@0.5', 'mAP'
    ])
